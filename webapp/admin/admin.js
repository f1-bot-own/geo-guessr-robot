/**
 * GeoGuru & GeoGuessr Web Admin Dashboard JavaScript
 * Handles 2FA Auth, Telegram WebApp Auto-login, SSE Live Streaming,
 * Chart.js Visualizations, User Management, Broadcast Engine, and Logs.
 */

(function () {
  'use strict';

  // Application State
  const state = {
    user: null,
    token: null,
    activeTab: 'tabOverview',
    usersPage: 0,
    usersLimit: 25,
    usersTotal: 0,
    currentSearchQuery: '',
    sseSource: null,
    chartActivity: null,
    chartModes: null,
    logAutoScroll: true,
    broadcastPollTimer: null,
    otpTimerInterval: null,
  };

  // DOM Elements
  const el = {
    authScreen: document.getElementById('authScreen'),
    authStep1: document.getElementById('authStep1'),
    authStep2: document.getElementById('authStep2'),
    inputAdminId: document.getElementById('inputAdminId'),
    inputOtpCode: document.getElementById('inputOtpCode'),
    btnRequestOtp: document.getElementById('btnRequestOtp'),
    btnVerifyOtp: document.getElementById('btnVerifyOtp'),
    btnBackToStep1: document.getElementById('btnBackToStep1'),
    otpTimer: document.getElementById('otpTimer'),
    authErrorAlert: document.getElementById('authErrorAlert'),
    authErrorText: document.getElementById('authErrorText'),
    authSuccessAlert: document.getElementById('authSuccessAlert'),
    authSuccessText: document.getElementById('authSuccessText'),
    webappAutoLoginNotice: document.getElementById('webappAutoLoginNotice'),

    mainDashboard: document.getElementById('mainDashboard'),
    adminProfileName: document.getElementById('adminProfileName'),
    adminProfileId: document.getElementById('adminProfileId'),
    liveStatusDot: document.getElementById('liveStatusDot'),
    liveStatusText: document.getElementById('liveStatusText'),
    btnLogout: document.getElementById('btnLogout'),

    // KPI Cards
    statTotalUsers: document.getElementById('statTotalUsers'),
    statActiveToday: document.getElementById('statActiveToday'),
    statTotalGroups: document.getElementById('statTotalGroups'),
    statTotalGames: document.getElementById('statTotalGames'),
    statTotalAnswers: document.getElementById('statTotalAnswers'),
    statCorrectAnswers: document.getElementById('statCorrectAnswers'),
    statAccuracyPercent: document.getElementById('statAccuracyPercent'),
    liveTickerFeed: document.getElementById('liveTickerFeed'),
    btnClearTicker: document.getElementById('btnClearTicker'),

    // Users
    inputUserSearch: document.getElementById('inputUserSearch'),
    btnRefreshUsers: document.getElementById('btnRefreshUsers'),
    usersTableBody: document.getElementById('usersTableBody'),
    usersPaginationInfo: document.getElementById('usersPaginationInfo'),
    btnUsersPrev: document.getElementById('btnUsersPrev'),
    btnUsersNext: document.getElementById('btnUsersNext'),

    // Groups
    btnRefreshGroups: document.getElementById('btnRefreshGroups'),
    groupsTableBody: document.getElementById('groupsTableBody'),

    // Answers
    btnRefreshAnswers: document.getElementById('btnRefreshAnswers'),
    recentAnswersList: document.getElementById('recentAnswersList'),
    difficultQuestionsList: document.getElementById('difficultQuestionsList'),

    // Broadcast
    broadcastText: document.getElementById('broadcastText'),
    broadcastPhoto: document.getElementById('broadcastPhoto'),
    broadcastBtnText: document.getElementById('broadcastBtnText'),
    broadcastBtnUrl: document.getElementById('broadcastBtnUrl'),
    btnStartBroadcast: document.getElementById('btnStartBroadcast'),
    previewTextMessage: document.getElementById('previewTextMessage'),
    previewPhotoContainer: document.getElementById('previewPhotoContainer'),
    previewPhotoImg: document.getElementById('previewPhotoImg'),
    previewButtonContainer: document.getElementById('previewButtonContainer'),
    previewButton: document.getElementById('previewButton'),
    broadcastProgressBar: document.getElementById('broadcastProgressBar'),
    broadcastPercent: document.getElementById('broadcastPercent'),
    broadcastSentCount: document.getElementById('broadcastSentCount'),
    broadcastFailedCount: document.getElementById('broadcastFailedCount'),
    broadcastBlockedCount: document.getElementById('broadcastBlockedCount'),
    broadcastTotalCount: document.getElementById('broadcastTotalCount'),
    broadcastStatusTitle: document.getElementById('broadcastStatusTitle'),
    broadcastSpinner: document.getElementById('broadcastSpinner'),

    // Logs
    terminalWindow: document.getElementById('terminalWindow'),
    inputLogFilter: document.getElementById('inputLogFilter'),
    checkAutoScroll: document.getElementById('checkAutoScroll'),
    btnRefreshLogs: document.getElementById('btnRefreshLogs'),

    // Modals
    modalAdjustXp: document.getElementById('modalAdjustXp'),
    modalAdjustUserId: document.getElementById('modalAdjustUserId'),
    modalAdjustXpSubtitle: document.getElementById('modalAdjustXpSubtitle'),
    inputNewXp: document.getElementById('inputNewXp'),
    btnCancelAdjustXp: document.getElementById('btnCancelAdjustXp'),
    btnSaveAdjustXp: document.getElementById('btnSaveAdjustXp'),

    modalBanUser: document.getElementById('modalBanUser'),
    modalBanTitle: document.getElementById('modalBanTitle'),
    modalBanSubtitle: document.getElementById('modalBanSubtitle'),
    modalBanUserId: document.getElementById('modalBanUserId'),
    modalBanAction: document.getElementById('modalBanAction'),
    modalBanReasonContainer: document.getElementById('modalBanReasonContainer'),
    inputBanReason: document.getElementById('inputBanReason'),
    btnCancelBan: document.getElementById('btnCancelBan'),
    btnConfirmBan: document.getElementById('btnConfirmBan'),
  };

  // Helper: API Request with auth headers
  async function api(endpoint, options = {}) {
    options.headers = options.headers || {};
    if (state.token) {
      options.headers['Authorization'] = `Bearer ${state.token}`;
    }
    if (options.body && typeof options.body === 'object' && !(options.body instanceof FormData)) {
      options.headers['Content-Type'] = 'application/json';
      options.body = JSON.stringify(options.body);
    }
    options.credentials = 'same-origin';

    const resp = await fetch(endpoint, options);
    const data = await resp.json().catch(() => ({ ok: false, error: 'Server javobida xatolik' }));
    if (!resp.ok && !data.error) {
      data.error = `HTTP Error ${resp.status}`;
    }
    return data;
  }

  // Show error alert in auth modal
  function showAuthError(msg) {
    el.authErrorText.textContent = msg;
    el.authErrorAlert.classList.remove('hidden');
    el.authSuccessAlert.classList.add('hidden');
  }

  function showAuthSuccess(msg) {
    el.authSuccessText.textContent = msg;
    el.authSuccessAlert.classList.remove('hidden');
    el.authErrorAlert.classList.add('hidden');
  }

  function clearAuthAlerts() {
    el.authErrorAlert.classList.add('hidden');
    el.authSuccessAlert.classList.add('hidden');
  }

  // -------------------------------------------------------------
  // Authentication & Initialization
  // -------------------------------------------------------------

  async function checkExistingAuth() {
    // 1. Try Telegram WebApp auto-login if launched inside Telegram
    const tg = window.Telegram?.WebApp;
    if (tg && tg.initData && tg.initData.length > 10) {
      el.webappAutoLoginNotice.classList.remove('hidden');
      try {
        const resp = await api('/api/admin/verify-webapp', {
          method: 'POST',
          body: { init_data: tg.initData }
        });
        if (resp.ok) {
          state.user = resp.user;
          state.token = resp.token;
          loginSuccess();
          return;
        } else {
          el.webappAutoLoginNotice.classList.add('hidden');
          showAuthError(resp.error || "Telegram orqali admin ruxsati topilmadi.");
        }
      } catch (e) {
        el.webappAutoLoginNotice.classList.add('hidden');
      }
    }

    // 2. Try session cookie / me endpoint
    try {
      const resp = await api('/api/admin/me');
      if (resp.ok && resp.user) {
        state.user = resp.user;
        loginSuccess();
        return;
      }
    } catch (e) {
      // not logged in
    }

    // Show login screen
    el.authScreen.classList.remove('hidden');
  }

  function startOtpTimer(durationSeconds = 300) {
    clearInterval(state.otpTimerInterval);
    let remaining = durationSeconds;
    const update = () => {
      const m = Math.floor(remaining / 60);
      const s = remaining % 60;
      el.otpTimer.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
      if (remaining <= 0) {
        clearInterval(state.otpTimerInterval);
        el.otpTimer.textContent = "Muddati o'tdi";
      }
      remaining--;
    };
    update();
    state.otpTimerInterval = setInterval(update, 1000);
  }

  // Step 1: Request OTP
  el.btnRequestOtp.addEventListener('click', async () => {
    clearAuthAlerts();
    const userId = el.inputAdminId.value.trim();
    if (!userId) {
      showAuthError("Telegram Admin ID raqamini kiriting.");
      return;
    }

    el.btnRequestOtp.disabled = true;
    el.btnRequestOtp.innerHTML = `<i class="fa-solid fa-spinner fa-spin mr-2"></i> Yuborilmoqda...`;

    try {
      const res = await api('/api/admin/request-otp', {
        method: 'POST',
        body: { user_id: parseInt(userId, 10) }
      });

      if (res.ok) {
        showAuthSuccess("Tasdiqlash kodi Telegram botingizga yuborildi!");
        el.authStep1.classList.add('hidden');
        el.authStep2.classList.remove('hidden');
        el.inputOtpCode.focus();
        startOtpTimer(300);
      } else {
        showAuthError(res.error || "Xatolik yuz berdi");
      }
    } catch (err) {
      showAuthError("Server bilan bog'lanishda xatolik.");
    } finally {
      el.btnRequestOtp.disabled = false;
      el.btnRequestOtp.innerHTML = `<span>Kodni olish (Send 2FA Code)</span><i class="fa-solid fa-paper-plane text-xs"></i>`;
    }
  });

  el.btnBackToStep1.addEventListener('click', () => {
    clearAuthAlerts();
    clearInterval(state.otpTimerInterval);
    el.authStep2.classList.add('hidden');
    el.authStep1.classList.remove('hidden');
  });

  // Step 2: Verify OTP
  el.btnVerifyOtp.addEventListener('click', async () => {
    clearAuthAlerts();
    const userId = el.inputAdminId.value.trim();
    const otp = el.inputOtpCode.value.trim();
    if (!otp || otp.length !== 6) {
      showAuthError("6 xonali tasdiqlash kodini to'liq kiriting.");
      return;
    }

    el.btnVerifyOtp.disabled = true;
    el.btnVerifyOtp.innerHTML = `<i class="fa-solid fa-spinner fa-spin mr-2"></i> Tekshirilmoqda...`;

    try {
      const res = await api('/api/admin/verify-otp', {
        method: 'POST',
        body: { user_id: parseInt(userId, 10), otp: otp }
      });

      if (res.ok) {
        state.user = res.user;
        state.token = res.token;
        loginSuccess();
      } else {
        showAuthError(res.error || "Kiritilgan kod noto'g'ri yoki eskirgan.");
      }
    } catch (err) {
      showAuthError("Server bilan bog'lanishda xatolik.");
    } finally {
      el.btnVerifyOtp.disabled = false;
      el.btnVerifyOtp.innerHTML = `<span>Kirish (Login)</span><i class="fa-solid fa-arrow-right-to-bracket text-xs"></i>`;
    }
  });

  // Logout handler
  el.btnLogout.addEventListener('click', async () => {
    if (confirm("Haqiqatan ham boshqaruv panelidan chiqmoqchimisiz?")) {
      await api('/api/admin/logout', { method: 'POST' });
      if (state.sseSource) {
        state.sseSource.close();
      }
      location.reload();
    }
  });

  function loginSuccess() {
    el.authScreen.classList.add('hidden');
    el.mainDashboard.classList.remove('hidden');

    const u = state.user || {};
    el.adminProfileName.textContent = u.first_name || u.username || 'Admin';
    el.adminProfileId.textContent = `ID: ${u.user_id || u.id || '-'}`;

    // Initialize components
    initLiveStream();
    loadDashboardStats();
    setupNavigation();
    setupBroadcastPreview();
  }

  // -------------------------------------------------------------
  // SSE Live Stream
  // -------------------------------------------------------------

  function setStreamStatus(status) {
    el.liveStatusDot.className = 'pulse-dot ' + status;
    if (status === 'online') {
      el.liveStatusText.textContent = 'Jonli efir: Ulangan';
    } else if (status === 'connecting') {
      el.liveStatusText.textContent = 'Ulanmoqda...';
    } else {
      el.liveStatusText.textContent = 'Uzildi (Qayta ulanmoqda)';
    }
  }

  function initLiveStream() {
    if (state.sseSource) {
      state.sseSource.close();
    }

    setStreamStatus('connecting');
    const sseUrl = `/api/admin/live-stream${state.token ? '?token=' + encodeURIComponent(state.token) : ''}`;
    const sse = new EventSource(sseUrl);
    state.sseSource = sse;

    sse.addEventListener('connected', () => {
      setStreamStatus('online');
    });

    sse.addEventListener('open', () => {
      setStreamStatus('online');
    });

    sse.addEventListener('ping', () => {
      // heartbeat received
    });

    sse.addEventListener('answer', (e) => {
      try {
        const data = JSON.parse(e.data);
        addLiveTickerItem('answer', data);
        incrementAnswerCount(data.is_correct);
      } catch (err) {}
    });

    sse.addEventListener('answer_logged', (e) => {
      try {
        const data = JSON.parse(e.data);
        addLiveTickerItem('answer', data);
      } catch (err) {}
    });

    sse.addEventListener('user_banned', (e) => {
      try {
        const data = JSON.parse(e.data);
        addLiveTickerItem('ban', data);
      } catch (err) {}
    });

    sse.addEventListener('user_unbanned', (e) => {
      try {
        const data = JSON.parse(e.data);
        addLiveTickerItem('unban', data);
      } catch (err) {}
    });

    sse.addEventListener('xp_adjusted', (e) => {
      try {
        const data = JSON.parse(e.data);
        addLiveTickerItem('xp', data);
      } catch (err) {}
    });

    sse.addEventListener('broadcast_progress', (e) => {
      try {
        const data = JSON.parse(e.data);
        updateBroadcastProgressUI(data);
      } catch (err) {}
    });

    sse.addEventListener('broadcast_complete', (e) => {
      try {
        const data = JSON.parse(e.data);
        updateBroadcastCompleteUI(data);
      } catch (err) {}
    });

    sse.onerror = () => {
      setStreamStatus('offline');
    };
  }

  function addLiveTickerItem(type, data) {
    const feed = el.liveTickerFeed;
    if (feed.children.length === 1 && feed.children[0].textContent.includes('kutilmoqda')) {
      feed.innerHTML = '';
    }

    const timeStr = new Date().toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const div = document.createElement('div');
    div.className = 'event-item p-2.5 rounded-xl bg-gray-900/60 border border-white/5 flex items-center justify-between text-xs';

    if (type === 'answer') {
      const isCorrect = data.is_correct;
      div.innerHTML = `
        <div class="flex items-center space-x-2">
          <span class="w-6 h-6 rounded-lg ${isCorrect ? 'bg-emerald-500/20 text-emerald-400' : 'bg-rose-500/20 text-rose-400'} flex items-center justify-center text-[10px] font-bold">
            ${isCorrect ? '<i class="fa-solid fa-check"></i>' : '<i class="fa-solid fa-xmark"></i>'}
          </span>
          <div>
            <span class="font-semibold text-white">${escapeHtml(data.user_name || 'Foydalanuvchi ' + data.user_id)}</span>
            <span class="text-gray-400 text-[11px]">${isCorrect ? "to'g'ri javob berdi (+XP)" : "noto'g'ri javob berdi"}</span>
          </div>
        </div>
        <span class="text-[10px] text-gray-500 font-mono">${timeStr}</span>
      `;
    } else if (type === 'ban') {
      div.innerHTML = `
        <div class="flex items-center space-x-2">
          <span class="w-6 h-6 rounded-lg bg-rose-500/20 text-rose-400 flex items-center justify-center text-[10px]">
            <i class="fa-solid fa-ban"></i>
          </span>
          <div>
            <span class="font-semibold text-rose-300">User ${data.user_id}</span>
            <span class="text-gray-400 text-[11px]">bloklandi (${escapeHtml(data.reason || 'Sababsiz')})</span>
          </div>
        </div>
        <span class="text-[10px] text-gray-500 font-mono">${timeStr}</span>
      `;
    } else if (type === 'xp') {
      div.innerHTML = `
        <div class="flex items-center space-x-2">
          <span class="w-6 h-6 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center text-[10px]">
            <i class="fa-solid fa-star"></i>
          </span>
          <div>
            <span class="font-semibold text-amber-300">User ${data.user_id}</span>
            <span class="text-gray-400 text-[11px]">XP balli yangilandi: ${data.xp} XP</span>
          </div>
        </div>
        <span class="text-[10px] text-gray-500 font-mono">${timeStr}</span>
      `;
    }

    feed.prepend(div);
    if (feed.children.length > 30) {
      feed.removeChild(feed.lastChild);
    }
  }

  el.btnClearTicker.addEventListener('click', () => {
    el.liveTickerFeed.innerHTML = '<div class="text-xs text-gray-500 py-3 text-center">Jonli hodisalar kutilmoqda...</div>';
  });

  function incrementAnswerCount(isCorrect) {
    const total = parseInt(el.statTotalAnswers.textContent.replace(/\D/g, '') || 0, 10) + 1;
    el.statTotalAnswers.textContent = total.toLocaleString();
    if (isCorrect) {
      const correct = parseInt(el.statCorrectAnswers.textContent.replace(/\D/g, '') || 0, 10) + 1;
      el.statCorrectAnswers.textContent = correct.toLocaleString();
      const pct = ((correct / total) * 100).toFixed(1);
      el.statAccuracyPercent.textContent = `${pct}%`;
    }
  }

  // -------------------------------------------------------------
  // Tab Navigation
  // -------------------------------------------------------------

  function setupNavigation() {
    document.querySelectorAll('.nav-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const targetTabId = tab.dataset.tab;
        switchTab(targetTabId);
      });
    });
  }

  function switchTab(tabId) {
    state.activeTab = tabId;

    document.querySelectorAll('.nav-tab').forEach(btn => {
      if (btn.dataset.tab === tabId) {
        btn.className = 'nav-tab active flex items-center space-x-2 px-3.5 py-2 rounded-xl text-xs font-medium text-white bg-cyan-500/20 border border-cyan-500/30 transition';
      } else {
        btn.className = 'nav-tab flex items-center space-x-2 px-3.5 py-2 rounded-xl text-xs font-medium text-gray-400 hover:text-white hover:bg-white/5 border border-transparent transition';
      }
    });

    document.querySelectorAll('.tab-content').forEach(section => {
      section.classList.add('hidden');
    });

    const targetEl = document.getElementById(tabId);
    if (targetEl) {
      targetEl.classList.remove('hidden');
    }

    // Trigger tab data fetch
    if (tabId === 'tabOverview') {
      loadDashboardStats();
    } else if (tabId === 'tabUsers') {
      loadUsers();
    } else if (tabId === 'tabGroups') {
      loadGroups();
    } else if (tabId === 'tabAnswers') {
      loadAnswers();
    } else if (tabId === 'tabLogs') {
      loadLogs();
    }
  }

  // -------------------------------------------------------------
  // Tab 1: Overview & Charts
  // -------------------------------------------------------------

  async function loadDashboardStats() {
    const res = await api('/api/admin/stats');
    if (!res.ok || !res.stats) return;

    const s = res.stats;
    el.statTotalUsers.textContent = (s.total_users || 0).toLocaleString();
    el.statActiveToday.textContent = (s.active_today || 0).toLocaleString();
    el.statTotalGroups.textContent = (s.total_groups || 0).toLocaleString();
    el.statTotalGames.textContent = (s.total_games || 0).toLocaleString();
    el.statTotalAnswers.textContent = (s.total_answers || 0).toLocaleString();
    el.statCorrectAnswers.textContent = (s.correct_answers || 0).toLocaleString();
    el.statAccuracyPercent.textContent = `${s.accuracy_percent || 0}%`;

    renderActivityChart(s.activity_24h || []);
    renderModesChart(s.mode_distribution || []);
  }

  function renderActivityChart(activityData) {
    const ctx = document.getElementById('chartActivity24h');
    if (!ctx) return;

    const labels = activityData.map(d => d.hour_label || '');
    const counts = activityData.map(d => d.event_count || 0);

    // If empty, generate past 6 hours sample labels
    if (labels.length === 0) {
      for (let i = 5; i >= 0; i--) {
        const d = new Date(Date.now() - i * 3600 * 1000);
        labels.push(`${d.getHours()}:00`);
        counts.push(0);
      }
    }

    if (state.chartActivity) {
      state.chartActivity.destroy();
    }

    state.chartActivity = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Faol javoblar soni',
          data: counts,
          borderColor: '#06b6d4',
          backgroundColor: 'rgba(6, 182, 212, 0.15)',
          borderWidth: 2,
          fill: true,
          tension: 0.35,
          pointBackgroundColor: '#06b6d4',
          pointBorderColor: '#fff',
          pointRadius: 4,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#111928',
            titleColor: '#fff',
            bodyColor: '#cbd5e1',
            borderColor: 'rgba(255,255,255,0.1)',
            borderWidth: 1,
            padding: 10,
          }
        },
        scales: {
          x: {
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { color: '#94a3b8', font: { size: 10 } }
          },
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { color: '#94a3b8', font: { size: 10 }, stepSize: 1 }
          }
        }
      }
    });
  }

  function renderModesChart(modeDist) {
    const ctx = document.getElementById('chartModeDistribution');
    if (!ctx) return;

    let labels = modeDist.map(m => (m.mode || 'standard').toUpperCase());
    let counts = modeDist.map(m => m.match_count || 0);

    if (labels.length === 0) {
      labels = ['FLAGS', 'CAPITALS', 'STREETVIEW', 'ZAKOVAT'];
      counts = [1, 1, 1, 1];
    }

    if (state.chartModes) {
      state.chartModes.destroy();
    }

    state.chartModes = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          data: counts,
          backgroundColor: ['#06b6d4', '#3b82f6', '#10b981', '#a855f7', '#f59e0b', '#ec4899'],
          borderColor: '#0a0f1d',
          borderWidth: 3,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: '#cbd5e1', font: { size: 10 }, boxWidth: 10, padding: 12 }
          }
        },
        cutout: '70%',
      }
    });
  }

  // -------------------------------------------------------------
  // Tab 2: Users Management
  // -------------------------------------------------------------

  async function loadUsers() {
    el.usersTableBody.innerHTML = `<tr><td colspan="7" class="p-4 text-center text-gray-500">Yuklanmoqda...</td></tr>`;
    const offset = state.usersPage * state.usersLimit;
    const q = state.currentSearchQuery;

    let url = `/api/admin/users?limit=${state.usersLimit}&offset=${offset}`;
    if (q) url += `&query=${encodeURIComponent(q)}`;

    const res = await api(url);
    if (!res.ok) {
      el.usersTableBody.innerHTML = `<tr><td colspan="7" class="p-4 text-center text-rose-400">Foydalanuvchilarni yuklashda xatolik</td></tr>`;
      return;
    }

    state.usersTotal = res.total || 0;
    renderUsersTable(res.users || []);
    updateUsersPagination();
  }

  function renderUsersTable(users) {
    if (!users || users.length === 0) {
      el.usersTableBody.innerHTML = `<tr><td colspan="7" class="p-6 text-center text-gray-500">Hech qanday foydalanuvchi topilmadi.</td></tr>`;
      return;
    }

    el.usersTableBody.innerHTML = users.map(u => {
      const isBanned = Boolean(u.is_banned);
      const name = escapeHtml(u.first_name || 'Player');
      const username = u.username ? `@${escapeHtml(u.username)}` : `<span class="text-gray-500">-</span>`;

      return `
        <tr class="hover:bg-white/[0.02] transition">
          <td class="p-3.5 flex items-center space-x-2.5">
            <div class="w-8 h-8 rounded-full bg-cyan-600/30 text-cyan-300 font-bold flex items-center justify-center text-xs">
              ${name.charAt(0).toUpperCase()}
            </div>
            <div>
              <div class="font-medium text-white">${name}</div>
              <div class="text-[11px] text-gray-400">${username}</div>
            </div>
          </td>
          <td class="p-3.5 font-mono text-gray-300">${u.user_id}</td>
          <td class="p-3.5">
            <span class="px-2 py-0.5 rounded-md bg-purple-900/60 text-purple-300 border border-purple-700/50 text-[10px] font-semibold mr-1.5">
              Lvl ${u.level || 1}
            </span>
            <span class="text-gray-300 font-medium">${(u.xp || 0).toLocaleString()} XP</span>
          </td>
          <td class="p-3.5 text-gray-300">
            <span class="text-emerald-400 font-semibold">${u.games_won || 0}</span>
            <span class="text-gray-500">/</span>
            <span>${u.games_played || 0}</span>
          </td>
          <td class="p-3.5 text-gray-300">
            <span class="text-cyan-400 font-semibold">${u.correct_answers || 0}</span>
            <span class="text-gray-500">/</span>
            <span>${u.total_answers || 0}</span>
          </td>
          <td class="p-3.5">
            ${isBanned 
              ? `<span class="px-2 py-0.5 rounded-md bg-rose-950 text-rose-300 border border-rose-800 text-[10px] font-semibold">Bloklangan</span>` 
              : `<span class="px-2 py-0.5 rounded-md bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-semibold">Faol</span>`}
          </td>
          <td class="p-3.5 text-right space-x-1">
            <button class="btn-adjust-xp px-2 py-1 rounded-lg bg-white/5 hover:bg-cyan-500/20 text-cyan-300 hover:text-cyan-200 border border-white/10 transition"
              data-id="${u.user_id}" data-name="${name}" data-xp="${u.xp || 0}">
              <i class="fa-solid fa-star text-[10px] mr-1"></i> XP
            </button>
            <button class="btn-toggle-ban px-2 py-1 rounded-lg ${isBanned ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'} border border-white/10 transition"
              data-id="${u.user_id}" data-name="${name}" data-banned="${isBanned}">
              <i class="fa-solid ${isBanned ? 'fa-lock-open' : 'fa-ban'} text-[10px] mr-1"></i> ${isBanned ? 'Ochish' : 'Bloklash'}
            </button>
          </td>
        </tr>
      `;
    }).join('');

    // Attach row button events
    document.querySelectorAll('.btn-adjust-xp').forEach(b => {
      b.addEventListener('click', () => {
        openAdjustXpModal(b.dataset.id, b.dataset.name, b.dataset.xp);
      });
    });

    document.querySelectorAll('.btn-toggle-ban').forEach(b => {
      b.addEventListener('click', () => {
        const isBanned = b.dataset.banned === 'true';
        openBanModal(b.dataset.id, b.dataset.name, isBanned);
      });
    });
  }

  function updateUsersPagination() {
    const start = state.usersTotal === 0 ? 0 : state.usersPage * state.usersLimit + 1;
    const end = Math.min((state.usersPage + 1) * state.usersLimit, state.usersTotal);
    el.usersPaginationInfo.textContent = `${start}-${end} dan ${state.usersTotal} ta`;

    el.btnUsersPrev.disabled = state.usersPage === 0;
    el.btnUsersNext.disabled = end >= state.usersTotal;
  }

  el.btnUsersPrev.addEventListener('click', () => {
    if (state.usersPage > 0) {
      state.usersPage--;
      loadUsers();
    }
  });

  el.btnUsersNext.addEventListener('click', () => {
    if ((state.usersPage + 1) * state.usersLimit < state.usersTotal) {
      state.usersPage++;
      loadUsers();
    }
  });

  // Search input debounce
  let searchDebounce = null;
  el.inputUserSearch.addEventListener('input', (e) => {
    clearTimeout(searchDebounce);
    searchDebounce = setTimeout(() => {
      state.currentSearchQuery = e.target.value.trim();
      state.usersPage = 0;
      loadUsers();
    }, 350);
  });

  el.btnRefreshUsers.addEventListener('click', () => loadUsers());

  // Adjust XP Modal Logic
  function openAdjustXpModal(userId, name, currentXp) {
    el.modalAdjustUserId.value = userId;
    el.modalAdjustXpSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId}) | Hozirgi XP: ${currentXp}`;
    el.inputNewXp.value = currentXp;
    el.modalAdjustXp.classList.remove('hidden');
    el.inputNewXp.focus();
  }

  el.btnCancelAdjustXp.addEventListener('click', () => el.modalAdjustXp.classList.add('hidden'));

  el.btnSaveAdjustXp.addEventListener('click', async () => {
    const userId = el.modalAdjustUserId.value;
    const newXp = parseInt(el.inputNewXp.value, 10);
    if (isNaN(newXp) || newXp < 0) {
      alert("Yaroqli musbat son kiriting.");
      return;
    }

    const res = await api('/api/admin/users/adjust-xp', {
      method: 'POST',
      body: { user_id: parseInt(userId, 10), xp: newXp }
    });

    if (res.ok) {
      el.modalAdjustXp.classList.add('hidden');
      loadUsers();
    } else {
      alert(res.error || "XP yangilashda xatolik");
    }
  });

  // Ban / Unban Modal Logic
  function openBanModal(userId, name, isCurrentlyBanned) {
    el.modalBanUserId.value = userId;
    el.modalBanAction.value = isCurrentlyBanned ? 'unban' : 'ban';
    el.modalBanSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId})`;

    if (isCurrentlyBanned) {
      el.modalBanTitle.innerHTML = `<i class="fa-solid fa-lock-open text-emerald-400"></i><span>Foydalanuvchini Blokdan Chiqarish</span>`;
      el.modalBanReasonContainer.classList.add('hidden');
      el.btnConfirmBan.textContent = "Blokdan Ochish";
      el.btnConfirmBan.className = "w-1/2 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold transition";
    } else {
      el.modalBanTitle.innerHTML = `<i class="fa-solid fa-ban text-rose-500"></i><span>Foydalanuvchini Bloklash</span>`;
      el.modalBanReasonContainer.classList.remove('hidden');
      el.inputBanReason.value = "";
      el.btnConfirmBan.textContent = "Bloklash";
      el.btnConfirmBan.className = "w-1/2 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-semibold transition";
    }

    el.modalBanUser.classList.remove('hidden');
  }

  el.btnCancelBan.addEventListener('click', () => el.modalBanUser.classList.add('hidden'));

  el.btnConfirmBan.addEventListener('click', async () => {
    const userId = parseInt(el.modalBanUserId.value, 10);
    const action = el.modalBanAction.value;
    const isBan = action === 'ban';
    const reason = el.inputBanReason.value.trim();

    const res = await api('/api/admin/users/ban', {
      method: 'POST',
      body: {
        user_id: userId,
        ban: isBan,
        reason: reason
      }
    });

    if (res.ok) {
      el.modalBanUser.classList.add('hidden');
      loadUsers();
    } else {
      alert(res.error || "Amalni bajarishda xatolik");
    }
  });

  // -------------------------------------------------------------
  // Tab 3: Groups
  // -------------------------------------------------------------

  async function loadGroups() {
    el.groupsTableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-gray-500">Yuklanmoqda...</td></tr>`;
    const res = await api('/api/admin/groups?limit=50');
    if (!res.ok) {
      el.groupsTableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-rose-400">Guruhlarni yuklashda xatolik</td></tr>`;
      return;
    }

    const groups = res.groups || [];
    if (groups.length === 0) {
      el.groupsTableBody.innerHTML = `<tr><td colspan="6" class="p-6 text-center text-gray-500">Hozircha ulangan guruhlar mavjud emas.</td></tr>`;
      return;
    }

    el.groupsTableBody.innerHTML = groups.map(g => {
      const title = escapeHtml(g.title || 'Guruh');
      const lang = (g.language || 'en').toUpperCase();

      return `
        <tr class="hover:bg-white/[0.02] transition">
          <td class="p-3.5 font-medium text-white flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center text-xs">
              <i class="fa-solid fa-users"></i>
            </span>
            <span>${title}</span>
          </td>
          <td class="p-3.5 font-mono text-gray-400">${g.chat_id}</td>
          <td class="p-3.5">
            <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300 border border-white/5 text-[10px] font-mono">
              ${lang}
            </span>
          </td>
          <td class="p-3.5 font-semibold text-purple-400">${g.total_games || 0} ta</td>
          <td class="p-3.5 text-gray-300">${g.players_count || 0} nafar</td>
          <td class="p-3.5 font-semibold text-amber-400">${(g.total_group_score || 0).toLocaleString()}</td>
        </tr>
      `;
    }).join('');
  }

  el.btnRefreshGroups.addEventListener('click', () => loadGroups());

  // -------------------------------------------------------------
  // Tab 4: Answers & Questions
  // -------------------------------------------------------------

  async function loadAnswers() {
    el.recentAnswersList.innerHTML = `<div class="p-3 text-center text-gray-500 text-xs">Yuklanmoqda...</div>`;
    el.difficultQuestionsList.innerHTML = `<div class="p-3 text-center text-gray-500 text-xs">Yuklanmoqda...</div>`;

    const res = await api('/api/admin/answers?limit=30');
    if (!res.ok) return;

    // Recent Answers
    const answers = res.recent_answers || [];
    if (answers.length === 0) {
      el.recentAnswersList.innerHTML = `<div class="p-4 text-center text-gray-500 text-xs">Javoblar logi hozircha bo'sh.</div>`;
    } else {
      el.recentAnswersList.innerHTML = answers.map(a => {
        const isCorrect = Boolean(a.is_correct);
        const name = escapeHtml(a.first_name || 'Player');
        const qText = escapeHtml(a.question_text || 'Savol matni');
        const given = escapeHtml(a.user_answer || '-');
        const correct = escapeHtml(a.correct_answer || '-');
        const timeStr = a.created_at ? new Date(a.created_at).toLocaleTimeString('uz-UZ') : '';

        return `
          <div class="p-3 hover:bg-white/[0.02] flex items-start justify-between space-x-2 text-xs">
            <div class="space-y-1">
              <div class="flex items-center space-x-2">
                <span class="font-semibold text-white">${name}</span>
                <span class="px-1.5 py-0.2 rounded text-[10px] ${isCorrect ? 'bg-emerald-950 text-emerald-300 border border-emerald-800' : 'bg-rose-950 text-rose-300 border border-rose-800'}">
                  ${isCorrect ? 'To\'g\'ri' : 'Noto\'g\'ri'}
                </span>
                <span class="text-[10px] text-gray-500">${timeStr}</span>
              </div>
              <div class="text-gray-300 text-[11px]">${qText}</div>
              <div class="text-[11px] text-gray-400">
                Javob: <span class="${isCorrect ? 'text-emerald-400 font-medium' : 'text-rose-400 line-through'}">${given}</span>
                ${!isCorrect && correct !== '-' ? ` <span class="text-emerald-400">(${correct})</span>` : ''}
              </div>
            </div>
            <div class="w-5 h-5 rounded-full ${isCorrect ? 'bg-emerald-500/20 text-emerald-400' : 'bg-rose-500/20 text-rose-400'} flex items-center justify-center text-[10px] shrink-0">
              <i class="fa-solid ${isCorrect ? 'fa-check' : 'fa-xmark'}"></i>
            </div>
          </div>
        `;
      }).join('');
    }

    // Difficult Questions
    const questions = res.difficult_questions || [];
    if (questions.length === 0) {
      el.difficultQuestionsList.innerHTML = `<div class="p-4 text-center text-gray-500 text-xs">Yetarlicha javob berilgan savollar yo'q.</div>`;
    } else {
      el.difficultQuestionsList.innerHTML = questions.map(q => {
        const text = escapeHtml(q.question_text || '');
        const acc = q.accuracy_pct || 0;
        const attempts = q.attempts || 0;

        let badgeColor = 'bg-rose-950 text-rose-300 border-rose-800';
        if (acc >= 40) badgeColor = 'bg-amber-950 text-amber-300 border-amber-800';

        return `
          <div class="p-3 hover:bg-white/[0.02] flex items-center justify-between space-x-2 text-xs">
            <div class="flex-1 pr-2">
              <div class="text-gray-200 font-medium">${text}</div>
              <div class="text-[10px] text-gray-400 mt-0.5">Urinishlar soni: ${attempts} ta</div>
            </div>
            <div class="text-right shrink-0">
              <span class="px-2 py-0.5 rounded border text-[10px] font-bold ${badgeColor}">
                ${acc}% aniqlik
              </span>
            </div>
          </div>
        `;
      }).join('');
    }
  }

  el.btnRefreshAnswers.addEventListener('click', () => loadAnswers());

  // -------------------------------------------------------------
  // Tab 5: Broadcast Composer & Preview
  // -------------------------------------------------------------

  function setupBroadcastPreview() {
    const updatePreview = () => {
      const text = el.broadcastText.value.trim();
      const photo = el.broadcastPhoto.value.trim();
      const btnText = el.broadcastBtnText.value.trim();
      const btnUrl = el.broadcastBtnUrl.value.trim();

      // Text preview (render basic html tags)
      if (!text) {
        el.previewTextMessage.innerHTML = '<span class="text-gray-400 italic">Xabar matni bu yerda ko\'rinadi...</span>';
      } else {
        // Sanitize and preserve telegram-supported tags
        el.previewTextMessage.innerHTML = renderTelegramHtml(text);
      }

      // Photo preview
      if (photo && photo.startsWith('http')) {
        el.previewPhotoImg.src = photo;
        el.previewPhotoContainer.classList.remove('hidden');
      } else {
        el.previewPhotoContainer.classList.add('hidden');
      }

      // Button preview
      if (btnText && btnUrl) {
        el.previewButton.textContent = btnText;
        el.previewButton.href = btnUrl;
        el.previewButtonContainer.classList.remove('hidden');
      } else {
        el.previewButtonContainer.classList.add('hidden');
      }
    };

    el.broadcastText.addEventListener('input', updatePreview);
    el.broadcastPhoto.addEventListener('input', updatePreview);
    el.broadcastBtnText.addEventListener('input', updatePreview);
    el.broadcastBtnUrl.addEventListener('input', updatePreview);
  }

  function renderTelegramHtml(raw) {
    let clean = escapeHtml(raw);
    clean = clean.replace(/&lt;b&gt;(.*?)&lt;\/b&gt;/gi, '<b>$1</b>');
    clean = clean.replace(/&lt;i&gt;(.*?)&lt;\/i&gt;/gi, '<i>$1</i>');
    clean = clean.replace(/&lt;code&gt;(.*?)&lt;\/code&gt;/gi, '<code class="bg-black/30 px-1 rounded">$1</code>');
    clean = clean.replace(/\n/g, '<br>');
    return clean;
  }

  el.btnStartBroadcast.addEventListener('click', async () => {
    const target = document.querySelector('input[name="broadcastTarget"]:checked')?.value || 'all';
    const text = el.broadcastText.value.trim();
    const photo = el.broadcastPhoto.value.trim() || null;
    const btnText = el.broadcastBtnText.value.trim() || null;
    const btnUrl = el.broadcastBtnUrl.value.trim() || null;

    if (!text) {
      alert("Xabar matnini kiriting!");
      return;
    }

    if (!confirm(`Haqiqatan ham ushbu xabarni "${target}" auditoriyasiga yubormoqchimisiz?`)) {
      return;
    }

    el.btnStartBroadcast.disabled = true;
    el.btnStartBroadcast.innerHTML = `<i class="fa-solid fa-spinner fa-spin mr-2"></i> Boshlanmoqda...`;

    try {
      const res = await api('/api/admin/broadcast', {
        method: 'POST',
        body: {
          target: target,
          text: text,
          photo_url: photo,
          button_text: btnText,
          button_url: btnUrl
        }
      });

      if (res.ok) {
        el.broadcastStatusTitle.textContent = "Xabarnoma holati: Boshlandi...";
        el.broadcastSpinner.classList.remove('hidden');
        pollBroadcastStatus(res.broadcast_id);
      } else {
        alert(res.error || "Xabarnomani boshlashda xatolik");
      }
    } catch (e) {
      alert("Server xatosi: " + e.message);
    } finally {
      el.btnStartBroadcast.disabled = false;
      el.btnStartBroadcast.innerHTML = `<i class="fa-solid fa-paper-plane text-xs"></i><span>Xabarnomani Yuborish</span>`;
    }
  });

  function updateBroadcastProgressUI(data) {
    const pct = data.progress_pct || (data.total > 0 ? Math.round(((data.sent + data.failed + data.blocked) / data.total) * 100) : 0);
    el.broadcastProgressBar.style.width = `${pct}%`;
    el.broadcastPercent.textContent = `${pct}%`;

    el.broadcastSentCount.textContent = data.sent || 0;
    el.broadcastFailedCount.textContent = data.failed || 0;
    el.broadcastBlockedCount.textContent = data.blocked || 0;
    el.broadcastTotalCount.textContent = data.total || 0;
    el.broadcastStatusTitle.textContent = `Yuborilmoqda: ${pct}%`;
  }

  function updateBroadcastCompleteUI(data) {
    el.broadcastProgressBar.style.width = '100%';
    el.broadcastPercent.textContent = '100%';
    el.broadcastSentCount.textContent = data.sent || 0;
    el.broadcastFailedCount.textContent = data.failed || 0;
    el.broadcastBlockedCount.textContent = data.blocked || 0;
    el.broadcastTotalCount.textContent = data.total || 0;
    el.broadcastStatusTitle.textContent = "Xabarnoma muvaffaqiyatli yakunlandi!";
    el.broadcastSpinner.classList.add('hidden');
    clearInterval(state.broadcastPollTimer);
  }

  function pollBroadcastStatus(broadcastId) {
    clearInterval(state.broadcastPollTimer);
    state.broadcastPollTimer = setInterval(async () => {
      const res = await api(`/api/admin/broadcast/status?broadcast_id=${broadcastId}`);
      if (res.ok && res.job) {
        const job = res.job;
        updateBroadcastProgressUI(job);
        if (job.status === 'completed' || job.status === 'cancelled') {
          updateBroadcastCompleteUI(job);
        }
      }
    }, 2000);
  }

  // -------------------------------------------------------------
  // Tab 6: Server Logs
  // -------------------------------------------------------------

  async function loadLogs() {
    const res = await api('/api/admin/logs?lines=150');
    if (!res.ok) return;

    const lines = res.lines || [];
    const filter = el.inputLogFilter.value.trim().toLowerCase();

    const filtered = filter ? lines.filter(l => l.toLowerCase().includes(filter)) : lines;
    if (filtered.length === 0) {
      el.terminalWindow.innerHTML = '<div class="text-gray-500 italic p-2">Loglar mavjud emas yoki filter mos kelmadi.</div>';
      return;
    }

    el.terminalWindow.innerHTML = filtered.map(l => {
      let cls = 'info';
      if (l.includes('[ERROR]') || l.includes('CRITICAL')) cls = 'error';
      else if (l.includes('[WARNING]')) cls = 'warning';
      return `<div class="log-line ${cls}">${escapeHtml(l)}</div>`;
    }).join('');

    if (el.checkAutoScroll.checked) {
      el.terminalWindow.scrollTop = el.terminalWindow.scrollHeight;
    }
  }

  el.btnRefreshLogs.addEventListener('click', () => loadLogs());
  el.inputLogFilter.addEventListener('input', () => loadLogs());

  // Utility: Escape HTML
  function escapeHtml(text) {
    if (!text) return '';
    return String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Start Application
  checkExistingAuth();

})();

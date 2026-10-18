/**
 * GeoGuru & GeoGuessr Web Admin Dashboard JavaScript
 * Handles 2FA Auth, Telegram WebApp Auto-login, SSE Live Streaming,
 * Atlas Telemetry Daemon Terminal, User Account Management Modal,
 * Chart.js Visualizations, Broadcast Engine, and Audit Logs.
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
    strict2fa: localStorage.getItem('geoguru_strict_2fa') === 'true',
    eventsBuffer: [], // buffer up to 250 events
    activeUserProfileId: null,
    tickerInterval: null,
    overviewSearchFilter: '',
    answersSearchFilter: '',
    answersHistoryQuery: '',
    answersHistoryMode: 'all',
    answersHistoryCorrect: 'all',
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
    toggleStrict2fa: document.getElementById('toggleStrict2fa'),
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

    // Atlas Telemetry - Overview Tab
    atlasBodyOverview: document.getElementById('atlasBodyOverview'),
    atlasSearchOverview: document.getElementById('atlasSearchOverview'),
    btnClearAtlasOverview: document.getElementById('btnClearAtlasOverview'),
    atlasCountOverview: document.getElementById('atlasCountOverview'),
    atlasAutoScrollOverview: document.getElementById('atlasAutoScrollOverview'),

    // Admin Logins Audit Log Table
    loginsTableBody: document.getElementById('loginsTableBody'),
    btnRefreshLogins: document.getElementById('btnRefreshLogins'),

    // Users Tab
    inputUserSearch: document.getElementById('inputUserSearch'),
    btnRefreshUsers: document.getElementById('btnRefreshUsers'),
    usersTableBody: document.getElementById('usersTableBody'),
    usersPaginationInfo: document.getElementById('usersPaginationInfo'),
    btnUsersPrev: document.getElementById('btnUsersPrev'),
    btnUsersNext: document.getElementById('btnUsersNext'),
    btnRefreshRecentUsers: document.getElementById('btnRefreshRecentUsers'),
    recentUsersTableBody: document.getElementById('recentUsersTableBody'),

    // Groups Tab
    btnRefreshGroups: document.getElementById('btnRefreshGroups'),
    groupsTableBody: document.getElementById('groupsTableBody'),

    // Atlas Telemetry - Answers Tab
    atlasBodyAnswers: document.getElementById('atlasBodyAnswers'),
    atlasSearchAnswers: document.getElementById('atlasSearchAnswers'),
    btnClearAtlasAnswers: document.getElementById('btnClearAtlasAnswers'),
    atlasCountAnswers: document.getElementById('atlasCountAnswers'),
    atlasAutoScrollAnswers: document.getElementById('atlasAutoScrollAnswers'),

    // Answers Tab Content & Filters
    btnRefreshAnswers: document.getElementById('btnRefreshAnswers'),
    inputAnswerFilterQuery: document.getElementById('inputAnswerFilterQuery'),
    selectAnswerFilterMode: document.getElementById('selectAnswerFilterMode'),
    selectAnswerFilterCorrect: document.getElementById('selectAnswerFilterCorrect'),
    recentAnswersList: document.getElementById('recentAnswersList'),
    difficultQuestionsList: document.getElementById('difficultQuestionsList'),

    // Broadcast Tab
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

    // Server Logs Tab
    terminalWindow: document.getElementById('terminalWindow'),
    inputLogFilter: document.getElementById('inputLogFilter'),
    checkAutoScroll: document.getElementById('checkAutoScroll'),
    btnRefreshLogs: document.getElementById('btnRefreshLogs'),

    // Full User Profile Modal
    modalUserProfile: document.getElementById('modalUserProfile'),
    btnCloseUserProfile: document.getElementById('btnCloseUserProfile'),
    userModalAvatar: document.getElementById('userModalAvatar'),
    userModalName: document.getElementById('userModalName'),
    userModalStatusBadge: document.getElementById('userModalStatusBadge'),
    userModalUsername: document.getElementById('userModalUsername'),
    userModalId: document.getElementById('userModalId'),
    userModalRegistered: document.getElementById('userModalRegistered'),
    userModalScore: document.getElementById('userModalScore'),
    userModalXp: document.getElementById('userModalXp'),
    userModalLevel: document.getElementById('userModalLevel'),
    userModalWinRate: document.getElementById('userModalWinRate'),
    userModalAccuracy: document.getElementById('userModalAccuracy'),
    userModalStreak: document.getElementById('userModalStreak'),
    userModalBtnAdjustPoints: document.getElementById('userModalBtnAdjustPoints'),
    userModalBtnAdjustXp: document.getElementById('userModalBtnAdjustXp'),
    userModalBtnSetLevel: document.getElementById('userModalBtnSetLevel'),
    userModalBtnBanToggle: document.getElementById('userModalBtnBanToggle'),
    userModalBtnBanText: document.getElementById('userModalBtnBanText'),
    userModalBtnResetStats: document.getElementById('userModalBtnResetStats'),
    userModalAnswersCount: document.getElementById('userModalAnswersCount'),
    userModalAnswersTableBody: document.getElementById('userModalAnswersTableBody'),

    // Adjust Points Modal
    modalAdjustPoints: document.getElementById('modalAdjustPoints'),
    modalAdjustPointsSubtitle: document.getElementById('modalAdjustPointsSubtitle'),
    modalAdjustPointsUserId: document.getElementById('modalAdjustPointsUserId'),
    inputNewPoints: document.getElementById('inputNewPoints'),
    btnCancelAdjustPoints: document.getElementById('btnCancelAdjustPoints'),
    btnSaveAdjustPoints: document.getElementById('btnSaveAdjustPoints'),

    // Adjust XP Modal
    modalAdjustXp: document.getElementById('modalAdjustXp'),
    modalAdjustUserId: document.getElementById('modalAdjustUserId'),
    modalAdjustXpSubtitle: document.getElementById('modalAdjustXpSubtitle'),
    inputNewXp: document.getElementById('inputNewXp'),
    btnCancelAdjustXp: document.getElementById('btnCancelAdjustXp'),
    btnSaveAdjustXp: document.getElementById('btnSaveAdjustXp'),

    // Set Level Modal
    modalSetLevel: document.getElementById('modalSetLevel'),
    modalSetLevelSubtitle: document.getElementById('modalSetLevelSubtitle'),
    modalSetLevelUserId: document.getElementById('modalSetLevelUserId'),
    inputNewLevel: document.getElementById('inputNewLevel'),
    btnCancelSetLevel: document.getElementById('btnCancelSetLevel'),
    btnSaveSetLevel: document.getElementById('btnSaveSetLevel'),

    // Ban / Unban Modal
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

  // Safe User Name Formatter (Fixes lone "." bug)
  function formatUserName(userOrName, userId, username) {
    let name = '';
    let id = userId;
    let uname = username;

    if (typeof userOrName === 'object' && userOrName !== null) {
      name = userOrName.first_name || userOrName.name || userOrName.user_name || '';
      id = id || userOrName.user_id || userOrName.id;
      uname = uname || userOrName.username;
    } else if (typeof userOrName === 'string') {
      name = userOrName;
    }

    name = (name || '').trim();
    // Check if name is empty or consists purely of dots, commas, underscores, dashes, spaces
    const isLonePunct = !name || /^[\.\,\-\_\s\*\#\@\~]+$/.test(name);
    if (!isLonePunct) {
      return name;
    }
    if (uname) {
      return `@${uname}`;
    }
    if (id) {
      return `User #${id}`;
    }
    return 'Foydalanuvchi';
  }

  // Format relative timestamp ("Just now", "5s ago", "2m ago")
  function getRelativeTime(timestamp) {
    if (!timestamp) return 'Just now';
    const now = Date.now();
    let ts = timestamp;
    if (typeof timestamp === 'string') {
      ts = new Date(timestamp).getTime();
    } else if (typeof timestamp === 'number' && timestamp < 1e11) {
      ts = timestamp * 1000;
    }
    if (isNaN(ts) || ts <= 0) return 'Just now';

    const diffSec = Math.max(0, Math.floor((now - ts) / 1000));
    if (diffSec < 4) return 'Just now';
    if (diffSec < 60) return `${diffSec}s ago`;
    const diffMin = Math.floor(diffSec / 60);
    if (diffMin < 60) return `${diffMin}m ago`;
    const diffHours = Math.floor(diffMin / 60);
    if (diffHours < 24) return `${diffHours}h ago`;
    const diffDays = Math.floor(diffHours / 24);
    return `${diffDays}d ago`;
  }

  // Map category to CSS badge class
  function getCategoryBadgeClass(category) {
    const cat = (category || 'ZAKOVAT').toUpperCase();
    const map = {
      'ZAKOVAT': 'badge-zakovat',
      'GEOGRAPHY': 'badge-geography',
      'COSMOS': 'badge-cosmos',
      'SCIENCE': 'badge-science',
      'HISTORY': 'badge-history',
      'SOLO': 'badge-solo',
      'GROUP': 'badge-group',
      'DUEL': 'badge-duel',
    };
    return map[cat] || 'badge-zakovat';
  }

  // Format clean date string (YYYY-MM-DD HH:mm:ss)
  function formatDate(isoStr) {
    if (!isoStr) return '-';
    try {
      const d = new Date(isoStr);
      if (isNaN(d.getTime())) return isoStr;
      return d.toLocaleString('uz-UZ', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });
    } catch {
      return isoStr;
    }
  }

  // Show alerts in auth modal
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
    // 0. Initialize Strict 2FA toggle UI
    if (el.toggleStrict2fa) {
      el.toggleStrict2fa.checked = state.strict2fa;
      el.toggleStrict2fa.addEventListener('change', (e) => {
        state.strict2fa = e.target.checked;
        localStorage.setItem('geoguru_strict_2fa', state.strict2fa ? 'true' : 'false');
      });
    }

    // When Strict 2FA is active, force explicit OTP request screen!
    if (state.strict2fa) {
      el.authScreen.classList.remove('hidden');
      el.webappAutoLoginNotice.classList.add('hidden');
      return;
    }

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
      try {
        await api('/api/admin/logout', { method: 'POST' });
      } catch {}
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
    el.adminProfileName.textContent = formatUserName(u, u.user_id, u.username);
    el.adminProfileId.textContent = `ID: ${u.user_id || u.id || '-'}`;

    // Initialize relative time updater
    if (state.tickerInterval) clearInterval(state.tickerInterval);
    state.tickerInterval = setInterval(updateRelativeTimes, 4000);

    // Initialize all components
    initLiveStream();
    loadDashboardStats();
    loadAdminLogins();
    setupNavigation();
    setupAtlasControls();
    setupAnswersFilters();
    setupBroadcastPreview();
    setupModals();
  }

  // -------------------------------------------------------------
  // SSE Live Stream & Atlas Telemetry Daemon
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
      // heartbeat
    });

    sse.addEventListener('answer', (e) => {
      try {
        const data = JSON.parse(e.data);
        handleIncomingAnswerEvent(data);
      } catch (err) {}
    });

    sse.addEventListener('answer_logged', (e) => {
      try {
        const data = JSON.parse(e.data);
        handleIncomingAnswerEvent(data);
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

  function handleIncomingAnswerEvent(data) {
    // Normalize event object
    const safeName = formatUserName(data.user_name || data.first_name, data.user_id, data.username);
    const isCorrect = Boolean(data.is_correct);
    const category = (data.category || 'ZAKOVAT').toUpperCase();
    const chatTag = data.chat_tag || (data.chat_id && data.chat_id < 0 ? `[Guruh: ${Math.abs(data.chat_id)}]` : '[Shaxsiy]');
    const points = data.points !== undefined ? data.points : (isCorrect ? 100 : -20);
    const xp = data.xp !== undefined ? data.xp : (isCorrect ? 25 : 0);
    const nodeHash = data.node_hash || `tg-dc${(Math.abs(Number(data.user_id) || 1) % 5) + 1} · #${String(data.user_id || '0000').slice(-4)}`;
    const timestamp = data.timestamp || Date.now();

    const normalized = {
      id: data.id || `evt-${Date.now()}-${Math.random().toString(36).substr(2, 6)}`,
      user_id: data.user_id,
      user_name: safeName,
      username: data.username,
      question_text: data.question_text || '',
      is_correct: isCorrect,
      user_answer: data.user_answer || '',
      correct_answer: data.correct_answer || '',
      category: category,
      chat_tag: chatTag,
      points: points,
      xp: xp,
      node_hash: nodeHash,
      timestamp: timestamp,
    };

    // Buffer management (keep max 250 events)
    state.eventsBuffer.unshift(normalized);
    if (state.eventsBuffer.length > 250) {
      state.eventsBuffer.pop();
    }

    // Render to Atlas Terminals
    renderAtlasEventRow(normalized);
    updateAtlasCounters();

    // Update KPI ticker and counters
    addLiveTickerItem('answer', { ...data, user_name: safeName });
    incrementAnswerCount(isCorrect);
  }

  // Build Atlas Terminal Row HTML matching Image 3
  function createAtlasRowElement(evt) {
    const relTime = getRelativeTime(evt.timestamp);
    const badgeClass = getCategoryBadgeClass(evt.category);
    const safeName = escapeHtml(evt.user_name);
    const qSnippet = evt.question_text ? escapeHtml(evt.question_text.length > 38 ? evt.question_text.slice(0, 36) + '...' : evt.question_text) : 'savol';

    const div = document.createElement('div');
    div.className = 'atlas-row';
    div.dataset.id = evt.id;
    div.dataset.timestamp = typeof evt.timestamp === 'number' ? evt.timestamp : new Date(evt.timestamp).getTime();
    div.dataset.userId = evt.user_id;

    div.innerHTML = `
      <span class="atlas-time">${relTime}</span>
      <span class="atlas-badge ${badgeClass}">[${escapeHtml(evt.category)}]</span>
      <span class="atlas-location font-mono">${escapeHtml(evt.chat_tag)}</span>
      <div class="atlas-desc">
        <span class="user-tag cursor-pointer hover:underline" data-user-id="${evt.user_id}">${safeName}</span>
        <span class="action-arrow">→</span>
        <span class="question-snippet">${qSnippet}</span>
        <span class="result-check ${evt.is_correct ? 'text-emerald-400' : 'text-rose-400'}">
          ${evt.is_correct ? "to'g'ri javob" : "noto'g'ri"}
        </span>
        <span class="score-pill ${evt.is_correct ? 'correct' : 'incorrect'}">
          ${evt.is_correct ? `+${evt.points} ball, +${evt.xp} XP` : `${evt.points} ball`}
        </span>
      </div>
      <span class="atlas-node-hash font-mono">${escapeHtml(evt.node_hash)}</span>
    `;

    // Make clicking the row or user tag open Full User Profile Modal
    div.addEventListener('click', (e) => {
      openUserProfileModal(evt.user_id);
    });

    return div;
  }

  function matchesAtlasFilter(evt, query) {
    if (!query) return true;
    const q = query.toLowerCase();
    return (
      (evt.user_name && evt.user_name.toLowerCase().includes(q)) ||
      String(evt.user_id).includes(q) ||
      (evt.category && evt.category.toLowerCase().includes(q)) ||
      (evt.chat_tag && evt.chat_tag.toLowerCase().includes(q)) ||
      (evt.question_text && evt.question_text.toLowerCase().includes(q)) ||
      (evt.node_hash && evt.node_hash.toLowerCase().includes(q))
    );
  }

  function renderAtlasEventRow(evt) {
    // 1. Overview Terminal
    if (el.atlasBodyOverview && matchesAtlasFilter(evt, state.overviewSearchFilter)) {
      if (el.atlasBodyOverview.children.length === 1 && el.atlasBodyOverview.children[0].textContent.includes('kutilmoqda')) {
        el.atlasBodyOverview.innerHTML = '';
      }
      const rowOverview = createAtlasRowElement(evt);
      el.atlasBodyOverview.prepend(rowOverview);
      if (el.atlasBodyOverview.children.length > 150) {
        el.atlasBodyOverview.removeChild(el.atlasBodyOverview.lastChild);
      }
      if (el.atlasAutoScrollOverview && el.atlasAutoScrollOverview.checked) {
        el.atlasBodyOverview.scrollTop = 0;
      }
    }

    // 2. Answers Terminal
    if (el.atlasBodyAnswers && matchesAtlasFilter(evt, state.answersSearchFilter)) {
      if (el.atlasBodyAnswers.children.length === 1 && el.atlasBodyAnswers.children[0].textContent.includes('kutilmoqda')) {
        el.atlasBodyAnswers.innerHTML = '';
      }
      const rowAnswers = createAtlasRowElement(evt);
      el.atlasBodyAnswers.prepend(rowAnswers);
      if (el.atlasBodyAnswers.children.length > 150) {
        el.atlasBodyAnswers.removeChild(el.atlasBodyAnswers.lastChild);
      }
      if (el.atlasAutoScrollAnswers && el.atlasAutoScrollAnswers.checked) {
        el.atlasBodyAnswers.scrollTop = 0;
      }
    }
  }

  function reRenderAtlasTerminal(terminalType) {
    const isOverview = terminalType === 'overview';
    const container = isOverview ? el.atlasBodyOverview : el.atlasBodyAnswers;
    const query = isOverview ? state.overviewSearchFilter : state.answersSearchFilter;
    if (!container) return;

    container.innerHTML = '';
    const filtered = state.eventsBuffer.filter(e => matchesAtlasFilter(e, query));
    if (filtered.length === 0) {
      container.innerHTML = `<div class="text-xs text-gray-500 py-6 text-center font-mono">Mos keluvchi hodisalar topilmadi.</div>`;
      return;
    }

    filtered.forEach(evt => {
      container.appendChild(createAtlasRowElement(evt));
    });
  }

  function updateAtlasCounters() {
    const countStr = state.eventsBuffer.length.toString();
    if (el.atlasCountOverview) el.atlasCountOverview.textContent = countStr;
    if (el.atlasCountAnswers) el.atlasCountAnswers.textContent = countStr;
  }

  function updateRelativeTimes() {
    document.querySelectorAll('.atlas-row').forEach(row => {
      const ts = Number(row.dataset.timestamp);
      if (ts) {
        const timeEl = row.querySelector('.atlas-time');
        if (timeEl) timeEl.textContent = getRelativeTime(ts);
      }
    });
  }

  function setupAtlasControls() {
    // Overview Terminal search & clear
    if (el.atlasSearchOverview) {
      el.atlasSearchOverview.addEventListener('input', (e) => {
        state.overviewSearchFilter = e.target.value.trim();
        reRenderAtlasTerminal('overview');
      });
    }
    if (el.btnClearAtlasOverview) {
      el.btnClearAtlasOverview.addEventListener('click', () => {
        state.eventsBuffer = [];
        updateAtlasCounters();
        if (el.atlasBodyOverview) {
          el.atlasBodyOverview.innerHTML = `<div class="text-xs text-gray-500 py-6 text-center font-mono">Jonli hodisalar kutilmoqda va buferlanmoqda...</div>`;
        }
        if (el.atlasBodyAnswers) {
          el.atlasBodyAnswers.innerHTML = `<div class="text-xs text-gray-500 py-6 text-center font-mono">Jonli hodisalar kutilmoqda va buferlanmoqda...</div>`;
        }
      });
    }

    // Answers Terminal search & clear
    if (el.atlasSearchAnswers) {
      el.atlasSearchAnswers.addEventListener('input', (e) => {
        state.answersSearchFilter = e.target.value.trim();
        reRenderAtlasTerminal('answers');
      });
    }
    if (el.btnClearAtlasAnswers) {
      el.btnClearAtlasAnswers.addEventListener('click', () => {
        state.eventsBuffer = [];
        updateAtlasCounters();
        if (el.atlasBodyOverview) {
          el.atlasBodyOverview.innerHTML = `<div class="text-xs text-gray-500 py-6 text-center font-mono">Jonli hodisalar kutilmoqda va buferlanmoqda...</div>`;
        }
        if (el.atlasBodyAnswers) {
          el.atlasBodyAnswers.innerHTML = `<div class="text-xs text-gray-500 py-6 text-center font-mono">Jonli hodisalar kutilmoqda va buferlanmoqda...</div>`;
        }
      });
    }
  }

  function addLiveTickerItem(type, data) {
    const feed = el.liveTickerFeed;
    if (!feed) return;
    if (feed.children.length === 1 && feed.children[0].textContent.includes('kutilmoqda')) {
      feed.innerHTML = '';
    }

    const timeStr = new Date().toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const div = document.createElement('div');
    div.className = 'event-item p-2.5 rounded-xl bg-gray-900/60 border border-white/5 flex items-center justify-between text-xs cursor-pointer hover:border-cyan-500/30 transition';

    const safeName = formatUserName(data.user_name || data.first_name, data.user_id, data.username);

    if (type === 'answer') {
      const isCorrect = data.is_correct;
      div.innerHTML = `
        <div class="flex items-center space-x-2">
          <span class="w-6 h-6 rounded-lg ${isCorrect ? 'bg-emerald-500/20 text-emerald-400' : 'bg-rose-500/20 text-rose-400'} flex items-center justify-center text-[10px] font-bold">
            ${isCorrect ? '<i class="fa-solid fa-check"></i>' : '<i class="fa-solid fa-xmark"></i>'}
          </span>
          <div>
            <span class="font-semibold text-white">${escapeHtml(safeName)}</span>
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
    } else if (type === 'unban') {
      div.innerHTML = `
        <div class="flex items-center space-x-2">
          <span class="w-6 h-6 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-[10px]">
            <i class="fa-solid fa-lock-open"></i>
          </span>
          <div>
            <span class="font-semibold text-emerald-300">User ${data.user_id}</span>
            <span class="text-gray-400 text-[11px]">blokdan chiqarildi</span>
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

    if (data.user_id) {
      div.addEventListener('click', () => openUserProfileModal(data.user_id));
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
    if (!el.statTotalAnswers) return;
    const total = parseInt(el.statTotalAnswers.textContent.replace(/\D/g, '') || 0, 10) + 1;
    el.statTotalAnswers.textContent = total.toLocaleString();
    if (isCorrect && el.statCorrectAnswers) {
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
      loadAdminLogins();
    } else if (tabId === 'tabUsers') {
      loadUsers();
      loadRecentUsers();
    } else if (tabId === 'tabGroups') {
      loadGroups();
    } else if (tabId === 'tabAnswers') {
      loadAnswersHistory();
      loadDifficultQuestions();
    } else if (tabId === 'tabLogs') {
      loadLogs();
    }
  }

  // -------------------------------------------------------------
  // Tab 1: Overview, Charts & Admin Logins Audit
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
      labels = ['ZAKOVAT', 'GEOGRAPHY', 'COSMOS', 'SCIENCE', 'HISTORY'];
      counts = [35, 25, 18, 12, 10];
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
          backgroundColor: ['#a855f7', '#06b6d4', '#6366f1', '#10b981', '#f59e0b', '#ec4899'],
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

  // Load Admin Logins Audit Log
  async function loadAdminLogins() {
    if (!el.loginsTableBody) return;
    el.loginsTableBody.innerHTML = `<tr><td colspan="7" class="p-4 text-center text-gray-500 font-sans">Yuklanmoqda...</td></tr>`;

    const res = await api('/api/admin/logins?limit=50');
    if (!res.ok) {
      el.loginsTableBody.innerHTML = `<tr><td colspan="7" class="p-4 text-center text-rose-400 font-sans">Loginlar tarixini yuklashda xatolik</td></tr>`;
      return;
    }

    const logins = res.logins || [];
    if (logins.length === 0) {
      el.loginsTableBody.innerHTML = `<tr><td colspan="7" class="p-6 text-center text-gray-500 font-sans">Hozircha admin loginlari qayd etilmagan.</td></tr>`;
      return;
    }

    el.loginsTableBody.innerHTML = logins.map(l => {
      const timeStr = formatDate(l.created_at);
      const safeAdminName = formatUserName(l.username, l.user_id, l.username);
      const ip = escapeHtml(l.ip_address || '127.0.0.1');
      const authMethod = escapeHtml(l.auth_method || '2FA_OTP');
      const ua = escapeHtml(l.user_agent || 'Unknown Client');
      const shortUa = ua.length > 40 ? ua.slice(0, 38) + '...' : ua;

      let methodBadge = 'bg-cyan-950 text-cyan-300 border-cyan-800';
      if (authMethod.includes('WEBAPP')) methodBadge = 'bg-emerald-950 text-emerald-300 border-emerald-800';
      else if (authMethod.includes('SESSION')) methodBadge = 'bg-purple-950 text-purple-300 border-purple-800';

      return `
        <tr class="hover:bg-white/[0.02] transition">
          <td class="p-3 text-gray-400">${timeStr}</td>
          <td class="p-3 text-cyan-400 font-bold">${l.user_id}</td>
          <td class="p-3 text-white font-sans font-medium">${safeAdminName}</td>
          <td class="p-3 text-gray-300 flex items-center space-x-1.5">
            <i class="fa-solid fa-network-wired text-cyan-500 text-[10px]"></i>
            <span>${ip}</span>
          </td>
          <td class="p-3">
            <span class="px-2 py-0.5 rounded text-[10px] font-sans font-semibold border ${methodBadge}">
              ${authMethod}
            </span>
          </td>
          <td class="p-3 text-gray-400" title="${ua}">
            <span class="font-sans text-[11px]">${shortUa}</span>
          </td>
          <td class="p-3 text-right">
            <span class="px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-sans font-semibold">
              <i class="fa-solid fa-check text-[9px] mr-1"></i> Muvaffaqiyatli
            </span>
          </td>
        </tr>
      `;
    }).join('');
  }

  if (el.btnRefreshLogins) {
    el.btnRefreshLogins.addEventListener('click', () => loadAdminLogins());
  }

  // -------------------------------------------------------------
  // Tab 2: Users Management & Recent Users Table
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
      const safeName = formatUserName(u, u.user_id, u.username);
      const username = u.username ? `@${escapeHtml(u.username)}` : `<span class="text-gray-500">-</span>`;

      return `
        <tr class="hover:bg-white/[0.02] transition cursor-pointer" data-id="${u.user_id}">
          <td class="p-3.5 flex items-center space-x-2.5 user-cell" data-id="${u.user_id}">
            <div class="w-8 h-8 rounded-full bg-cyan-600/30 text-cyan-300 font-bold flex items-center justify-center text-xs">
              ${safeName.charAt(0).toUpperCase()}
            </div>
            <div>
              <div class="font-medium text-white hover:text-cyan-400 transition">${escapeHtml(safeName)}</div>
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
          <td class="p-3.5 text-right space-x-1" onclick="event.stopPropagation()">
            <button class="btn-user-profile px-2 py-1 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/25 text-cyan-300 border border-cyan-500/20 transition"
              data-id="${u.user_id}" title="To'liq profilni ko'rish">
              <i class="fa-solid fa-address-card text-[10px] mr-1"></i> Profil
            </button>
            <button class="btn-adjust-xp px-2 py-1 rounded-lg bg-white/5 hover:bg-cyan-500/20 text-cyan-300 hover:text-cyan-200 border border-white/10 transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-xp="${u.xp || 0}">
              <i class="fa-solid fa-star text-[10px] mr-1"></i> XP
            </button>
            <button class="btn-toggle-ban px-2 py-1 rounded-lg ${isBanned ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'} border border-white/10 transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-banned="${isBanned}">
              <i class="fa-solid ${isBanned ? 'fa-lock-open' : 'fa-ban'} text-[10px] mr-1"></i> ${isBanned ? 'Ochish' : 'Bloklash'}
            </button>
          </td>
        </tr>
      `;
    }).join('');

    // Attach row click to open full profile modal
    el.usersTableBody.querySelectorAll('tr').forEach(tr => {
      tr.addEventListener('click', () => {
        const id = tr.dataset.id;
        if (id) openUserProfileModal(id);
      });
    });

    // Attach button events
    el.usersTableBody.querySelectorAll('.btn-user-profile').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openUserProfileModal(b.dataset.id);
      });
    });

    el.usersTableBody.querySelectorAll('.btn-adjust-xp').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openAdjustXpModal(b.dataset.id, b.dataset.name, b.dataset.xp);
      });
    });

    el.usersTableBody.querySelectorAll('.btn-toggle-ban').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        const isBanned = b.dataset.banned === 'true';
        openBanModal(b.dataset.id, b.dataset.name, isBanned);
      });
    });
  }

  // Load Recent 50 Users Table
  async function loadRecentUsers() {
    if (!el.recentUsersTableBody) return;
    el.recentUsersTableBody.innerHTML = `<tr><td colspan="7" class="p-4 text-center text-gray-500">Yuklanmoqda...</td></tr>`;

    const res = await api('/api/admin/users/recent?limit=50');
    if (!res.ok) {
      el.recentUsersTableBody.innerHTML = `<tr><td colspan="7" class="p-4 text-center text-rose-400">Yangi foydalanuvchilarni yuklashda xatolik</td></tr>`;
      return;
    }

    const users = res.recent_users || [];
    if (users.length === 0) {
      el.recentUsersTableBody.innerHTML = `<tr><td colspan="7" class="p-6 text-center text-gray-500">Yangi foydalanuvchilar topilmadi.</td></tr>`;
      return;
    }

    el.recentUsersTableBody.innerHTML = users.map(u => {
      const isBanned = Boolean(u.is_banned);
      const safeName = formatUserName(u, u.user_id, u.username);
      const username = u.username ? `@${escapeHtml(u.username)}` : `<span class="text-gray-500">-</span>`;
      const regTime = formatDate(u.created_at);
      const lang = (u.language_code || 'uz').toUpperCase();

      return `
        <tr class="hover:bg-white/[0.02] transition cursor-pointer" data-id="${u.user_id}">
          <td class="p-3 flex items-center space-x-2.5">
            <div class="w-7 h-7 rounded-full bg-emerald-600/30 text-emerald-300 font-bold flex items-center justify-center text-xs">
              ${safeName.charAt(0).toUpperCase()}
            </div>
            <div>
              <div class="font-medium text-white hover:text-cyan-400 transition">${escapeHtml(safeName)}</div>
              <div class="text-[11px] text-gray-400">${username}</div>
            </div>
          </td>
          <td class="p-3 font-mono text-cyan-400">${u.user_id}</td>
          <td class="p-3 font-mono text-gray-400 text-xs">${regTime}</td>
          <td class="p-3">
            <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300 border border-white/5 text-[10px] font-mono">${lang}</span>
          </td>
          <td class="p-3 text-gray-300">
            <span class="px-2 py-0.5 rounded bg-purple-900/60 text-purple-300 border border-purple-700/50 text-[10px] font-semibold mr-1">
              Lvl ${u.level || 1}
            </span>
            <span class="text-xs font-medium">${(u.xp || 0).toLocaleString()} XP</span>
          </td>
          <td class="p-3">
            ${isBanned 
              ? `<span class="px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 text-[10px] font-semibold">Bloklangan</span>` 
              : `<span class="px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-semibold">Faol</span>`}
          </td>
          <td class="p-3 text-right" onclick="event.stopPropagation()">
            <button class="btn-recent-profile px-2.5 py-1 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/25 text-cyan-300 border border-cyan-500/20 text-xs transition"
              data-id="${u.user_id}">
              <i class="fa-solid fa-address-card mr-1 text-[10px]"></i> Profil
            </button>
          </td>
        </tr>
      `;
    }).join('');

    // Attach click handlers
    el.recentUsersTableBody.querySelectorAll('tr').forEach(tr => {
      tr.addEventListener('click', () => {
        const id = tr.dataset.id;
        if (id) openUserProfileModal(id);
      });
    });

    el.recentUsersTableBody.querySelectorAll('.btn-recent-profile').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openUserProfileModal(b.dataset.id);
      });
    });
  }

  if (el.btnRefreshRecentUsers) {
    el.btnRefreshRecentUsers.addEventListener('click', () => loadRecentUsers());
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

  let searchDebounce = null;
  el.inputUserSearch.addEventListener('input', (e) => {
    clearTimeout(searchDebounce);
    searchDebounce = setTimeout(() => {
      state.currentSearchQuery = e.target.value.trim();
      state.usersPage = 0;
      loadUsers();
    }, 350);
  });

  el.btnRefreshUsers.addEventListener('click', () => {
    loadUsers();
    loadRecentUsers();
  });

  // -------------------------------------------------------------
  // Full User Profile Modal Logic
  // -------------------------------------------------------------

  async function openUserProfileModal(userId) {
    if (!userId) return;
    state.activeUserProfileId = userId;

    // Reset and show modal loader state
    el.userModalAvatar.textContent = '...';
    el.userModalName.textContent = 'Yuklanmoqda...';
    el.userModalUsername.textContent = '@...';
    el.userModalId.textContent = userId;
    el.userModalRegistered.textContent = "Ro'yxatdan: ...";
    el.userModalAnswersTableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-gray-500 font-sans">Javoblar tarixi yuklanmoqda...</td></tr>`;
    el.modalUserProfile.classList.remove('hidden');

    const res = await api(`/api/admin/users/${userId}/full`);
    if (!res.ok || !res.profile) {
      alert(res.error || "Foydalanuvchi ma'lumotlarini yuklashda xatolik");
      el.modalUserProfile.classList.add('hidden');
      return;
    }

    const u = res.profile.user || {};
    const history = res.profile.history || [];
    const safeName = formatUserName(u, u.user_id, u.username);
    const isBanned = Boolean(u.is_banned);

    // Populate Header
    el.userModalAvatar.textContent = safeName.charAt(0).toUpperCase();
    el.userModalName.textContent = safeName;
    el.userModalUsername.textContent = u.username ? `@${u.username}` : `(username yo'q)`;
    el.userModalId.textContent = u.user_id;
    el.userModalRegistered.textContent = `Ro'yxatdan: ${formatDate(u.created_at)}`;

    if (isBanned) {
      el.userModalStatusBadge.className = 'px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30';
      el.userModalStatusBadge.textContent = 'Bloklangan';
      el.userModalBtnBanText.textContent = '🔓 Blokdan ochish';
    } else {
      el.userModalStatusBadge.className = 'px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
      el.userModalStatusBadge.textContent = 'Faol';
      el.userModalBtnBanText.textContent = '🚫 Bloklash';
    }

    // Populate Stats Cards
    el.userModalScore.textContent = (u.score || 0).toLocaleString();
    el.userModalXp.textContent = `${(u.xp || 0).toLocaleString()} XP`;
    el.userModalLevel.textContent = `${u.level || 1}-daraja`;
    el.userModalWinRate.textContent = `${u.win_rate !== undefined ? u.win_rate : (u.games_played > 0 ? Math.round((u.games_won / u.games_played) * 100) : 0)}%`;
    el.userModalAccuracy.textContent = `${u.correct_answers || 0} / ${u.total_answers || 0} (${u.accuracy_pct || 0}%)`;
    el.userModalStreak.textContent = `${u.streak || 0} (Max: ${u.best_streak || 0})`;

    // Populate Top 100 Answer History Table
    el.userModalAnswersCount.textContent = `${history.length} ta javob`;
    if (history.length === 0) {
      el.userModalAnswersTableBody.innerHTML = `<tr><td colspan="6" class="p-6 text-center text-gray-500 font-sans">Ushbu foydalanuvchi hali savollarga javob bermagan.</td></tr>`;
    } else {
      el.userModalAnswersTableBody.innerHTML = history.map(h => {
        const isCorrect = Boolean(h.is_correct);
        const timeStr = formatDate(h.created_at);
        const cat = (h.category || 'ZAKOVAT').toUpperCase();
        const badgeClass = getCategoryBadgeClass(cat);
        const qText = escapeHtml(h.question_text || '-');
        const userAns = escapeHtml(h.user_answer || '-');
        const corrAns = escapeHtml(h.correct_answer || '-');
        const points = h.points_awarded !== undefined ? h.points_awarded : (isCorrect ? 100 : -20);
        const xp = h.xp_awarded !== undefined ? h.xp_awarded : (isCorrect ? 25 : 0);

        return `
          <tr class="hover:bg-white/[0.02] transition">
            <td class="p-3 text-gray-400 font-sans text-xs">${timeStr}</td>
            <td class="p-3">
              <span class="atlas-badge ${badgeClass}">[${cat}]</span>
            </td>
            <td class="p-3 text-gray-200 font-sans text-xs max-w-xs truncate" title="${qText}">${qText}</td>
            <td class="p-3 font-sans text-xs">
              <span class="${isCorrect ? 'text-emerald-300 font-medium' : 'text-rose-400 line-through'}">${userAns}</span>
              ${!isCorrect && corrAns !== '-' ? `<span class="text-emerald-400 ml-1">(${corrAns})</span>` : ''}
            </td>
            <td class="p-3">
              <span class="score-pill ${isCorrect ? 'correct' : 'incorrect'}">
                ${isCorrect ? 'To\'g\'ri' : 'Noto\'g\'ri'}
              </span>
            </td>
            <td class="p-3 text-right font-sans">
              <span class="${isCorrect ? 'text-emerald-400 font-bold' : 'text-rose-400'}">
                ${isCorrect ? `+${points}b, +${xp}XP` : `${points}b`}
              </span>
            </td>
          </tr>
        `;
      }).join('');
    }

    // Bind modal actions for this active user
    el.userModalBtnAdjustPoints.onclick = () => openAdjustPointsModal(u.user_id, safeName, u.score || 0);
    el.userModalBtnAdjustXp.onclick = () => openAdjustXpModal(u.user_id, safeName, u.xp || 0);
    el.userModalBtnSetLevel.onclick = () => openSetLevelModal(u.user_id, safeName, u.level || 1);
    el.userModalBtnBanToggle.onclick = () => openBanModal(u.user_id, safeName, isBanned);
    el.userModalBtnResetStats.onclick = () => confirmResetUserStats(u.user_id, safeName);
  }

  el.btnCloseUserProfile.addEventListener('click', () => {
    el.modalUserProfile.classList.add('hidden');
    state.activeUserProfileId = null;
  });

  // Modal 1: Adjust Points
  function openAdjustPointsModal(userId, name, currentPoints) {
    el.modalAdjustPointsUserId.value = userId;
    el.modalAdjustPointsSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId}) | Hozirgi ball: ${currentPoints}`;
    el.inputNewPoints.value = currentPoints;
    el.modalAdjustPoints.classList.remove('hidden');
    el.inputNewPoints.focus();
  }

  el.btnCancelAdjustPoints.addEventListener('click', () => el.modalAdjustPoints.classList.add('hidden'));

  el.btnSaveAdjustPoints.addEventListener('click', async () => {
    const userId = el.modalAdjustPointsUserId.value;
    const newPoints = parseInt(el.inputNewPoints.value, 10);
    if (isNaN(newPoints) || newPoints < 0) {
      alert("Yaroqli musbat ball kiriting.");
      return;
    }

    const res = await api('/api/admin/users/adjust-points', {
      method: 'POST',
      body: { user_id: parseInt(userId, 10), points: newPoints }
    });

    if (res.ok) {
      el.modalAdjustPoints.classList.add('hidden');
      loadUsers();
      if (state.activeUserProfileId == userId) {
        openUserProfileModal(userId);
      }
    } else {
      alert(res.error || "Ballarni yangilashda xatolik");
    }
  });

  // Modal 2: Adjust XP
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
      if (state.activeUserProfileId == userId) {
        openUserProfileModal(userId);
      }
    } else {
      alert(res.error || "XP yangilashda xatolik");
    }
  });

  // Modal 3: Set Level
  function openSetLevelModal(userId, name, currentLevel) {
    el.modalSetLevelUserId.value = userId;
    el.modalSetLevelSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId}) | Hozirgi daraja: ${currentLevel}`;
    el.inputNewLevel.value = currentLevel;
    el.modalSetLevel.classList.remove('hidden');
    el.inputNewLevel.focus();
  }

  el.btnCancelSetLevel.addEventListener('click', () => el.modalSetLevel.classList.add('hidden'));

  el.btnSaveSetLevel.addEventListener('click', async () => {
    const userId = el.modalSetLevelUserId.value;
    const newLevel = parseInt(el.inputNewLevel.value, 10);
    if (isNaN(newLevel) || newLevel < 1 || newLevel > 100) {
      alert("Daraja 1 dan 100 gacha bo'lishi kerak.");
      return;
    }

    const res = await api('/api/admin/users/set-level', {
      method: 'POST',
      body: { user_id: parseInt(userId, 10), level: newLevel }
    });

    if (res.ok) {
      el.modalSetLevel.classList.add('hidden');
      loadUsers();
      if (state.activeUserProfileId == userId) {
        openUserProfileModal(userId);
      }
    } else {
      alert(res.error || "Darajani yangilashda xatolik");
    }
  });

  // Modal 4: Ban / Unban
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
      loadRecentUsers();
      if (state.activeUserProfileId == userId) {
        openUserProfileModal(userId);
      }
    } else {
      alert(res.error || "Amalni bajarishda xatolik");
    }
  });

  // Action: Reset User Stats
  async function confirmResetUserStats(userId, name) {
    if (!confirm(`DIQQAT! Foydalanuvchi "${name}" (ID: ${userId}) ning barcha ballari, XP, darajasi va g'alaba hisoblarini nollashni tasdiqlaysizmi? Bu amalni ortga qaytarib bo'lmaydi!`)) {
      return;
    }

    const res = await api('/api/admin/users/reset-stats', {
      method: 'POST',
      body: { user_id: parseInt(userId, 10) }
    });

    if (res.ok) {
      alert("Foydalanuvchi statistikasi muvaffaqiyatli nollashdi!");
      loadUsers();
      loadRecentUsers();
      if (state.activeUserProfileId == userId) {
        openUserProfileModal(userId);
      }
    } else {
      alert(res.error || "Statistikani nollashda xatolik yuz berdi");
    }
  }

  function setupModals() {
    // Backdrop click dismiss for modals
    [el.modalAdjustPoints, el.modalAdjustXp, el.modalSetLevel, el.modalBanUser].forEach(m => {
      if (!m) return;
      m.addEventListener('click', (e) => {
        if (e.target === m) m.classList.add('hidden');
      });
    });
  }

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
  // Tab 4: Answers & Questions (Filterable Answers History)
  // -------------------------------------------------------------

  function setupAnswersFilters() {
    let debounceTimer = null;
    if (el.inputAnswerFilterQuery) {
      el.inputAnswerFilterQuery.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
          state.answersHistoryQuery = e.target.value.trim();
          loadAnswersHistory();
        }, 300);
      });
    }

    if (el.selectAnswerFilterMode) {
      el.selectAnswerFilterMode.addEventListener('change', (e) => {
        state.answersHistoryMode = e.target.value;
        loadAnswersHistory();
      });
    }

    if (el.selectAnswerFilterCorrect) {
      el.selectAnswerFilterCorrect.addEventListener('change', (e) => {
        state.answersHistoryCorrect = e.target.value;
        loadAnswersHistory();
      });
    }

    if (el.btnRefreshAnswers) {
      el.btnRefreshAnswers.addEventListener('click', () => {
        loadAnswersHistory();
        loadDifficultQuestions();
      });
    }
  }

  async function loadAnswersHistory() {
    if (!el.recentAnswersList) return;
    el.recentAnswersList.innerHTML = `<div class="p-4 text-center text-gray-500 text-xs">Yuklanmoqda...</div>`;

    let url = `/api/admin/answers/history?limit=100`;
    if (state.answersHistoryQuery) url += `&query=${encodeURIComponent(state.answersHistoryQuery)}`;
    if (state.answersHistoryMode && state.answersHistoryMode !== 'all') url += `&mode=${encodeURIComponent(state.answersHistoryMode)}`;
    if (state.answersHistoryCorrect && state.answersHistoryCorrect !== 'all') url += `&correct=${encodeURIComponent(state.answersHistoryCorrect)}`;

    const res = await api(url);
    if (!res.ok) {
      el.recentAnswersList.innerHTML = `<div class="p-4 text-center text-rose-400 text-xs">Javoblarni yuklashda xatolik</div>`;
      return;
    }

    const answers = res.answers || [];
    if (answers.length === 0) {
      el.recentAnswersList.innerHTML = `<div class="p-6 text-center text-gray-500 text-xs font-sans">Belgilangan filter bo'yicha javoblar topilmadi.</div>`;
      return;
    }

    el.recentAnswersList.innerHTML = answers.map(a => {
      const isCorrect = Boolean(a.is_correct);
      const safeName = formatUserName(a.first_name || a.username, a.user_id, a.username);
      const qText = escapeHtml(a.question_text || 'Savol matni');
      const given = escapeHtml(a.user_answer || '-');
      const correct = escapeHtml(a.correct_answer || '-');
      const timeStr = formatDate(a.created_at);
      const cat = (a.category || 'ZAKOVAT').toUpperCase();
      const badgeClass = getCategoryBadgeClass(cat);
      const chatTag = a.chat_tag || (a.chat_id && a.chat_id < 0 ? `[Guruh: ${Math.abs(a.chat_id)}]` : '[Shaxsiy]');
      const points = a.points_awarded !== undefined ? a.points_awarded : (isCorrect ? 100 : -20);
      const xp = a.xp_awarded !== undefined ? a.xp_awarded : (isCorrect ? 25 : 0);

      return `
        <div class="p-3.5 hover:bg-white/[0.02] flex items-start justify-between space-x-3 transition cursor-pointer" onclick="window.openUserProfileFromAnswer(${a.user_id})">
          <div class="space-y-1.5 flex-1 overflow-hidden">
            <div class="flex items-center space-x-2 flex-wrap gap-y-1">
              <span class="font-semibold text-white hover:text-cyan-400 transition font-sans">${escapeHtml(safeName)}</span>
              <span class="atlas-badge ${badgeClass}">[${cat}]</span>
              <span class="text-[10px] text-gray-400 font-mono">${escapeHtml(chatTag)}</span>
              <span class="score-pill ${isCorrect ? 'correct' : 'incorrect'}">
                ${isCorrect ? 'To\'g\'ri' : 'Noto\'g\'ri'}
              </span>
              <span class="text-[10px] text-gray-500 font-mono ml-auto">${timeStr}</span>
            </div>
            <div class="text-gray-300 font-sans text-xs leading-relaxed">${qText}</div>
            <div class="text-[11px] font-sans text-gray-400 flex items-center space-x-2">
              <span>Javob: <strong class="${isCorrect ? 'text-emerald-400' : 'text-rose-400 line-through'}">${given}</strong></span>
              ${!isCorrect && correct !== '-' ? `<span class="text-emerald-400">(To'g'risi: ${correct})</span>` : ''}
              <span class="ml-auto font-mono ${isCorrect ? 'text-emerald-400 font-bold' : 'text-rose-400'}">
                ${isCorrect ? `+${points} ball, +${xp} XP` : `${points} ball`}
              </span>
            </div>
          </div>
          <div class="w-6 h-6 rounded-full ${isCorrect ? 'bg-emerald-500/20 text-emerald-400' : 'bg-rose-500/20 text-rose-400'} flex items-center justify-center text-[10px] shrink-0 mt-1">
            <i class="fa-solid ${isCorrect ? 'fa-check' : 'fa-xmark'}"></i>
          </div>
        </div>
      `;
    }).join('');
  }

  // Global helper for opening user profile from inline answer items
  window.openUserProfileFromAnswer = function(userId) {
    if (userId) openUserProfileModal(userId);
  };

  async function loadDifficultQuestions() {
    if (!el.difficultQuestionsList) return;
    el.difficultQuestionsList.innerHTML = `<div class="p-3 text-center text-gray-500 text-xs">Yuklanmoqda...</div>`;

    const res = await api('/api/admin/answers?limit=30');
    if (!res.ok) return;

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

  // -------------------------------------------------------------
  // Tab 5: Broadcast Composer & Preview
  // -------------------------------------------------------------

  function setupBroadcastPreview() {
    const updatePreview = () => {
      const text = el.broadcastText.value.trim();
      const photo = el.broadcastPhoto.value.trim();
      const btnText = el.broadcastBtnText.value.trim();
      const btnUrl = el.broadcastBtnUrl.value.trim();

      if (!text) {
        el.previewTextMessage.innerHTML = '<span class="text-gray-400 italic">Xabar matni bu yerda ko\'rinadi...</span>';
      } else {
        el.previewTextMessage.innerHTML = renderTelegramHtml(text);
      }

      if (photo && photo.startsWith('http')) {
        el.previewPhotoImg.src = photo;
        el.previewPhotoContainer.classList.remove('hidden');
      } else {
        el.previewPhotoContainer.classList.add('hidden');
      }

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

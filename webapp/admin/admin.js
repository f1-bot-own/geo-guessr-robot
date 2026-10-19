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

    // Overview Tab - Recent 50 Users Table
    inputRecentUserSearchOverview: document.getElementById('inputRecentUserSearchOverview'),
    btnRefreshRecentUsersOverview: document.getElementById('btnRefreshRecentUsersOverview'),
    recentUsersOverviewTableBody: document.getElementById('recentUsersOverviewTableBody'),

    // Admin Logins Audit Log Table (optional fallback)
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
  if (el.btnRequestOtp) {
    el.btnRequestOtp.addEventListener('click', async () => {
      clearAuthAlerts();
      const userId = el.inputAdminId ? el.inputAdminId.value.trim() : '';
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
          if (el.authStep1) el.authStep1.classList.add('hidden');
          if (el.authStep2) el.authStep2.classList.remove('hidden');
          if (el.inputOtpCode) el.inputOtpCode.focus();
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
  }

  if (el.btnBackToStep1) {
    el.btnBackToStep1.addEventListener('click', () => {
      clearAuthAlerts();
      clearInterval(state.otpTimerInterval);
      if (el.authStep2) el.authStep2.classList.add('hidden');
      if (el.authStep1) el.authStep1.classList.remove('hidden');
    });
  }

  // Step 2: Verify OTP
  if (el.btnVerifyOtp) {
    el.btnVerifyOtp.addEventListener('click', async () => {
      clearAuthAlerts();
      const userId = el.inputAdminId ? el.inputAdminId.value.trim() : '';
      const otp = el.inputOtpCode ? el.inputOtpCode.value.trim() : '';
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
  }

  // Logout handler
  if (el.btnLogout) {
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
  }

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
    loadRecentUsersOverview();
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
    const qSnippet = evt.question_text ? escapeHtml(evt.question_text.length > 40 ? evt.question_text.slice(0, 38) + '...' : evt.question_text) : 'savol';

    const div = document.createElement('div');
    div.className = 'atlas-row';
    div.dataset.id = evt.id;
    div.dataset.timestamp = typeof evt.timestamp === 'number' ? evt.timestamp : new Date(evt.timestamp).getTime();
    div.dataset.userId = evt.user_id;
    div.style.cssText = "background: #081729; border: 1px solid #122842; border-radius: 8px; padding: 8px 14px; display: flex; align-items: center; justify-content: space-between; gap: 12px; font-size: 12px; font-family: monospace; color: #e2e8f0; cursor: pointer; transition: all 0.15s ease;";

    const isCorr = Boolean(evt.is_correct);
    const resultCheckText = isCorr ? "to'g'ri javob" : "noto'g'ri";
    const resultCheckColor = isCorr ? "#34d399" : "#fb7185";
    const pillBg = isCorr ? "rgba(16, 185, 129, 0.18)" : "rgba(244, 63, 94, 0.18)";
    const pillColor = isCorr ? "#34d399" : "#fb7185";
    const pillBorder = isCorr ? "rgba(16, 185, 129, 0.35)" : "rgba(244, 63, 94, 0.35)";
    const pillText = isCorr ? `+${evt.points} ball, +${evt.xp} XP` : `${evt.points} ball`;

    div.innerHTML = `
      <span class="atlas-time" style="color: #64748b; width: 62px; flex-shrink: 0; font-size: 11px;">${relTime}</span>
      <span class="atlas-badge ${badgeClass}" style="padding: 2px 7px; border-radius: 4px; font-size: 10px; font-weight: 700; flex-shrink: 0; text-transform: uppercase;">[${escapeHtml(evt.category)}]</span>
      <span class="atlas-location" style="color: #38bdf8; font-size: 11px; font-weight: 500; flex-shrink: 0;">${escapeHtml(evt.chat_tag)}</span>
      <div class="atlas-desc" style="display: flex; align-items: center; gap: 7px; flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
        <span class="user-tag" style="color: #ffffff; font-weight: 600; flex-shrink: 0;" data-user-id="${evt.user_id}">${safeName}</span>
        <span class="action-arrow" style="color: #64748b; flex-shrink: 0;">→</span>
        <span class="question-snippet" style="color: #cbd5e1; flex-shrink: 1; overflow: hidden; text-overflow: ellipsis;">${qSnippet}</span>
        <span class="result-check" style="color: ${resultCheckColor}; font-weight: 600; flex-shrink: 0;">${resultCheckText}</span>
        <span class="score-pill ${isCorr ? 'correct' : 'incorrect'}" style="font-size: 10px; padding: 2px 7px; border-radius: 9999px; font-weight: 700; flex-shrink: 0; background: ${pillBg}; color: ${pillColor}; border: 1px solid ${pillBorder};">${pillText}</span>
      </div>
      <span class="atlas-node-hash" style="color: #0284c7; font-size: 11px; flex-shrink: 0;">${escapeHtml(evt.node_hash)}</span>
    `;

    // Make clicking anywhere on the row open Full User Profile Modal
    div.addEventListener('click', (e) => {
      if (evt.user_id) {
        openUserProfileModal(evt.user_id);
      }
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

  if (el.btnClearTicker && el.liveTickerFeed) {
    el.btnClearTicker.addEventListener('click', () => {
      el.liveTickerFeed.innerHTML = '<div class="text-xs text-gray-500 py-3 text-center">Jonli hodisalar kutilmoqda...</div>';
    });
  }

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
      loadRecentUsersOverview();
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
  // Overview Tab: Recent 50 Users (Qachon, soat nechida kirgani)
  // -------------------------------------------------------------

  let overviewRecentUsersData = [];

  async function loadRecentUsersOverview() {
    if (!el.recentUsersOverviewTableBody) return;
    el.recentUsersOverviewTableBody.innerHTML = `<tr><td colspan="8" class="p-6 text-center text-gray-500 font-sans">So'nggi 50 ta foydalanuvchilar yuklanmoqda...</td></tr>`;

    const res = await api('/api/admin/users/recent?limit=50');
    if (!res.ok) {
      el.recentUsersOverviewTableBody.innerHTML = `<tr><td colspan="8" class="p-6 text-center text-rose-400 font-sans">Yangi foydalanuvchilarni yuklashda xatolik</td></tr>`;
      return;
    }

    overviewRecentUsersData = res.recent_users || [];
    renderRecentUsersOverviewTable(overviewRecentUsersData);
  }

  function renderRecentUsersOverviewTable(users) {
    if (!el.recentUsersOverviewTableBody) return;
    if (!users || users.length === 0) {
      el.recentUsersOverviewTableBody.innerHTML = `<tr><td colspan="8" class="p-6 text-center text-gray-500 font-sans">Foydalanuvchilar topilmadi.</td></tr>`;
      return;
    }

    el.recentUsersOverviewTableBody.innerHTML = users.map(u => {
      const isBanned = Boolean(u.is_banned);
      const safeName = formatUserName(u, u.user_id, u.username);
      const username = u.username ? `@${escapeHtml(u.username)}` : `<span class="text-gray-500">-</span>`;
      const regTime = formatDate(u.created_at);
      const score = (u.total_score || u.score || 0).toLocaleString();
      const xp = (u.xp || 0).toLocaleString();
      const level = u.level || 1;
      const totalAnswers = u.total_answers || 0;
      const correctAnswers = u.correct_answers || 0;

      return `
        <tr class="hover:bg-white/[0.04] transition cursor-pointer" data-id="${u.user_id}">
          <td class="p-3 font-mono text-cyan-300 font-medium text-xs whitespace-nowrap">
            <i class="fa-regular fa-clock mr-1 text-gray-400"></i> ${regTime}
          </td>
          <td class="p-3">
            <div class="flex items-center space-x-2.5">
              <div class="w-7 h-7 rounded-full bg-emerald-600/30 text-emerald-300 font-bold flex items-center justify-center text-xs flex-shrink-0">
                ${safeName.charAt(0).toUpperCase()}
              </div>
              <div>
                <div class="font-medium text-white hover:text-cyan-400 transition">${escapeHtml(safeName)}</div>
                <div class="text-[11px] text-gray-400">${username}</div>
              </div>
            </div>
          </td>
          <td class="p-3 font-mono text-gray-300">${u.user_id}</td>
          <td class="p-3 font-mono text-amber-400 font-semibold">${score} ball</td>
          <td class="p-3 text-gray-300 whitespace-nowrap">
            <span class="px-2 py-0.5 rounded bg-purple-900/60 text-purple-300 border border-purple-700/50 text-[10px] font-semibold mr-1">
              Lvl ${level}
            </span>
            <span class="text-xs font-medium">${xp} XP</span>
          </td>
          <td class="p-3 text-gray-300 whitespace-nowrap">
            <span class="text-emerald-400 font-semibold">${correctAnswers}</span>
            <span class="text-gray-500">/</span>
            <span>${totalAnswers}</span>
          </td>
          <td class="p-3">
            ${isBanned 
              ? `<span class="px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 text-[10px] font-semibold">Bloklangan</span>` 
              : `<span class="px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px] font-semibold">Faol</span>`}
          </td>
          <td class="p-3 text-right space-x-1 whitespace-nowrap" onclick="event.stopPropagation()">
            <button class="btn-ov-profile px-2.5 py-1 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/25 text-cyan-300 border border-cyan-500/20 text-xs transition"
              data-id="${u.user_id}" title="Profilni ko'rish">
              <i class="fa-solid fa-address-card mr-1 text-[10px]"></i> Profil
            </button>
            <button class="btn-ov-points px-2 py-1 rounded-lg bg-amber-500/10 hover:bg-amber-500/25 text-amber-300 border border-amber-500/20 text-xs transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-score="${u.total_score || u.score || 0}" title="Ball o'zgartirish">
              <i class="fa-solid fa-trophy mr-1 text-[10px]"></i> Ball
            </button>
            <button class="btn-ov-level px-2 py-1 rounded-lg bg-purple-500/10 hover:bg-purple-500/25 text-purple-300 border border-purple-500/20 text-xs transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-level="${level}" title="Daraja o'rnatish">
              <i class="fa-solid fa-medal mr-1 text-[10px]"></i> Level
            </button>
            <button class="btn-ov-ban px-2 py-1 rounded-lg ${isBanned ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'} border border-white/10 text-xs transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-banned="${isBanned}" title="${isBanned ? 'Blokdan chiqarish' : 'Bloklash'}">
              <i class="fa-solid ${isBanned ? 'fa-lock-open' : 'fa-ban'} mr-1 text-[10px]"></i> ${isBanned ? 'Ochish' : 'Blok'}
            </button>
          </td>
        </tr>
      `;
    }).join('');

    // Row clicks open profile modal
    el.recentUsersOverviewTableBody.querySelectorAll('tr').forEach(tr => {
      tr.addEventListener('click', () => {
        const id = tr.dataset.id;
        if (id) openUserProfileModal(id);
      });
    });

    // Button clicks
    el.recentUsersOverviewTableBody.querySelectorAll('.btn-ov-profile').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openUserProfileModal(b.dataset.id);
      });
    });

    el.recentUsersOverviewTableBody.querySelectorAll('.btn-ov-points').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openAdjustPointsModal(b.dataset.id, b.dataset.name, b.dataset.score);
      });
    });

    el.recentUsersOverviewTableBody.querySelectorAll('.btn-ov-level').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openSetLevelModal(b.dataset.id, b.dataset.name, b.dataset.level);
      });
    });

    el.recentUsersOverviewTableBody.querySelectorAll('.btn-ov-ban').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        const isBanned = b.dataset.banned === 'true';
        openBanModal(b.dataset.id, b.dataset.name, isBanned);
      });
    });
  }

  if (el.btnRefreshRecentUsersOverview) {
    el.btnRefreshRecentUsersOverview.addEventListener('click', () => loadRecentUsersOverview());
  }

  if (el.inputRecentUserSearchOverview) {
    el.inputRecentUserSearchOverview.addEventListener('input', (e) => {
      const q = e.target.value.trim().toLowerCase();
      if (!q) {
        renderRecentUsersOverviewTable(overviewRecentUsersData);
        return;
      }
      const filtered = overviewRecentUsersData.filter(u => {
        const name = (u.first_name || u.clean_name || '').toLowerCase();
        const uname = (u.username || '').toLowerCase();
        const uid = String(u.user_id);
        return name.includes(q) || uname.includes(q) || uid.includes(q);
      });
      renderRecentUsersOverviewTable(filtered);
    });
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
          <td class="p-3.5 text-right space-x-1 whitespace-nowrap" onclick="event.stopPropagation()">
            <button class="btn-user-profile px-2 py-1 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/25 text-cyan-300 border border-cyan-500/20 text-xs transition"
              data-id="${u.user_id}" title="To'liq profilni ko'rish">
              <i class="fa-solid fa-address-card text-[10px] mr-1"></i> Profil
            </button>
            <button class="btn-adjust-points px-2 py-1 rounded-lg bg-amber-500/10 hover:bg-amber-500/25 text-amber-300 border border-amber-500/20 text-xs transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-score="${u.total_score || u.score || 0}" title="Ball o'zgartirish">
              <i class="fa-solid fa-trophy text-[10px] mr-1"></i> Ball
            </button>
            <button class="btn-set-level px-2 py-1 rounded-lg bg-purple-500/10 hover:bg-purple-500/25 text-purple-300 border border-purple-500/20 text-xs transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-level="${u.level || 1}" title="Daraja o'rnatish">
              <i class="fa-solid fa-medal text-[10px] mr-1"></i> Lvl
            </button>
            <button class="btn-adjust-xp px-2 py-1 rounded-lg bg-white/5 hover:bg-cyan-500/20 text-cyan-300 hover:text-cyan-200 border border-white/10 text-xs transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-xp="${u.xp || 0}" title="XP o'zgartirish">
              <i class="fa-solid fa-star text-[10px] mr-1"></i> XP
            </button>
            <button class="btn-toggle-ban px-2 py-1 rounded-lg ${isBanned ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'} border border-white/10 text-xs transition"
              data-id="${u.user_id}" data-name="${escapeHtml(safeName)}" data-banned="${isBanned}" title="${isBanned ? 'Blokdan chiqarish' : 'Bloklash'}">
              <i class="fa-solid ${isBanned ? 'fa-lock-open' : 'fa-ban'} text-[10px] mr-1"></i> ${isBanned ? 'Ochish' : 'Blok'}
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

    el.usersTableBody.querySelectorAll('.btn-adjust-points').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openAdjustPointsModal(b.dataset.id, b.dataset.name, b.dataset.score);
      });
    });

    el.usersTableBody.querySelectorAll('.btn-set-level').forEach(b => {
      b.addEventListener('click', (e) => {
        e.stopPropagation();
        openSetLevelModal(b.dataset.id, b.dataset.name, b.dataset.level);
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

  if (el.btnUsersPrev) {
    el.btnUsersPrev.addEventListener('click', () => {
      if (state.usersPage > 0) {
        state.usersPage--;
        loadUsers();
      }
    });
  }

  if (el.btnUsersNext) {
    el.btnUsersNext.addEventListener('click', () => {
      if ((state.usersPage + 1) * state.usersLimit < state.usersTotal) {
        state.usersPage++;
        loadUsers();
      }
    });
  }

  let searchDebounce = null;
  if (el.inputUserSearch) {
    el.inputUserSearch.addEventListener('input', (e) => {
      clearTimeout(searchDebounce);
      searchDebounce = setTimeout(() => {
        state.currentSearchQuery = e.target.value.trim();
        state.usersPage = 0;
        loadUsers();
      }, 350);
    });
  }

  if (el.btnRefreshUsers) {
    el.btnRefreshUsers.addEventListener('click', () => {
      loadUsers();
      loadRecentUsers();
      loadRecentUsersOverview();
    });
  }

  // -------------------------------------------------------------
  // Full User Profile Modal Logic
  // -------------------------------------------------------------

  async function openUserProfileModal(userId) {
    if (!userId) return;
    state.activeUserProfileId = userId;

    // Reset and show modal loader state
    if (el.userModalAvatar) el.userModalAvatar.textContent = '...';
    if (el.userModalName) el.userModalName.textContent = 'Yuklanmoqda...';
    if (el.userModalUsername) el.userModalUsername.textContent = '@...';
    if (el.userModalId) el.userModalId.textContent = userId;
    if (el.userModalRegistered) el.userModalRegistered.textContent = "Ro'yxatdan: ...";
    if (el.userModalAnswersTableBody) {
      el.userModalAnswersTableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-gray-500 font-sans">Javoblar tarixi yuklanmoqda...</td></tr>`;
    }
    if (el.modalUserProfile) {
      el.modalUserProfile.classList.remove('hidden');
    }

    try {
      const res = await api(`/api/admin/users/${userId}/full`);
      if (!res || !res.ok) {
        alert((res && res.error) || "Foydalanuvchi ma'lumotlarini yuklashda xatolik");
        if (el.modalUserProfile) el.modalUserProfile.classList.add('hidden');
        return;
      }

      const p = res.profile || res;
      const u = p.user || p;
      const stats = p.stats || {};
      const history = p.history || p.answers || p.recent_answers || [];
      const safeName = formatUserName(u, u.user_id || userId, u.username);
      const isBanned = Boolean(u.is_banned !== undefined ? u.is_banned : stats.is_banned);

      // Populate Header
      if (el.userModalAvatar) el.userModalAvatar.textContent = safeName.charAt(0).toUpperCase();
      if (el.userModalName) el.userModalName.textContent = safeName;
      if (el.userModalUsername) el.userModalUsername.textContent = u.username ? `@${u.username}` : `(username yo'q)`;
      if (el.userModalId) el.userModalId.textContent = u.user_id || userId;
      if (el.userModalRegistered) el.userModalRegistered.textContent = `Ro'yxatdan: ${formatDate(u.created_at || stats.created_at)}`;

      if (el.userModalStatusBadge) {
        if (isBanned) {
          el.userModalStatusBadge.className = 'px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30';
          el.userModalStatusBadge.textContent = 'Bloklangan';
          if (el.userModalBtnBanText) el.userModalBtnBanText.textContent = '🔓 Blokdan ochish';
        } else {
          el.userModalStatusBadge.className = 'px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
          el.userModalStatusBadge.textContent = 'Faol';
          if (el.userModalBtnBanText) el.userModalBtnBanText.textContent = '🚫 Bloklash';
        }
      }

      // Populate Stats Cards
      const rawScore = u.score !== undefined ? u.score : (u.total_score !== undefined ? u.total_score : (stats.total_score !== undefined ? stats.total_score : 0));
      const scoreVal = Number(rawScore) || 0;
      const rawXp = u.xp !== undefined ? u.xp : (stats.xp !== undefined ? stats.xp : 0);
      const xpVal = Number(rawXp) || 0;
      const rawLevel = u.level || stats.level || 1;
      const levelVal = Number(rawLevel) || 1;

      const rawWinRate = p.win_rate !== undefined ? p.win_rate : (stats.win_rate !== undefined ? stats.win_rate : (u.win_rate !== undefined ? u.win_rate : (u.games_played > 0 ? Math.round((u.games_won / u.games_played) * 100) : 0)));
      const winRateVal = Number(rawWinRate) || 0;

      const correctAnswers = u.correct_answers !== undefined ? u.correct_answers : (stats.correct_answers !== undefined ? stats.correct_answers : 0);
      const totalAnswers = u.total_answers !== undefined ? u.total_answers : (stats.total_answers !== undefined ? stats.total_answers : 0);
      const rawAccuracy = p.accuracy !== undefined ? p.accuracy : (stats.accuracy !== undefined ? stats.accuracy : (u.accuracy_pct !== undefined ? u.accuracy_pct : (totalAnswers > 0 ? Math.round((correctAnswers / totalAnswers) * 100) : 0)));
      const accuracyVal = Number(rawAccuracy) || 0;

      const currentStreak = u.streak !== undefined ? u.streak : (u.current_streak !== undefined ? u.current_streak : (stats.streak !== undefined ? stats.streak : (stats.current_streak || 0)));
      const bestStreak = u.best_streak !== undefined ? u.best_streak : (stats.best_streak || 0);

      if (el.userModalScore) el.userModalScore.textContent = scoreVal.toLocaleString();
      if (el.userModalXp) el.userModalXp.textContent = `${xpVal.toLocaleString()} XP`;
      if (el.userModalLevel) el.userModalLevel.textContent = `${levelVal}-daraja`;
      if (el.userModalWinRate) el.userModalWinRate.textContent = `${winRateVal}%`;
      if (el.userModalAccuracy) el.userModalAccuracy.textContent = `${correctAnswers} / ${totalAnswers} (${accuracyVal}%)`;
      if (el.userModalStreak) el.userModalStreak.textContent = `${currentStreak} (Max: ${bestStreak})`;

      // Populate Top 100 Answer History Table
      if (el.userModalAnswersCount) el.userModalAnswersCount.textContent = `${history.length} ta javob`;
      if (el.userModalAnswersTableBody) {
        if (history.length === 0) {
          el.userModalAnswersTableBody.innerHTML = `<tr><td colspan="6" class="p-6 text-center text-gray-500 font-sans">Ushbu foydalanuvchi hali savollarga javob bermagan.</td></tr>`;
        } else {
          el.userModalAnswersTableBody.innerHTML = history.map(h => {
            const isCorrect = Boolean(h.is_correct);
            const timeStr = formatDate(h.created_at);
            const cat = (h.category || h.mode || 'ZAKOVAT').toUpperCase();
            const badgeClass = getCategoryBadgeClass(cat);
            const qText = escapeHtml(h.question_text || h.question || '-');
            const userAns = escapeHtml(h.user_answer || h.selected_option || '-');
            const corrAns = escapeHtml(h.correct_answer || h.correct_option || '-');
            const points = h.points !== undefined ? h.points : (h.points_awarded !== undefined ? h.points_awarded : (isCorrect ? 100 : -20));
            const xp = h.xp !== undefined ? h.xp : (h.xp_awarded !== undefined ? h.xp_awarded : (isCorrect ? 25 : 0));

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
      }

      // Bind modal actions for this active user
      const targetUserId = u.user_id || userId;
      if (el.userModalBtnAdjustPoints) el.userModalBtnAdjustPoints.onclick = () => openAdjustPointsModal(targetUserId, safeName, scoreVal);
      if (el.userModalBtnAdjustXp) el.userModalBtnAdjustXp.onclick = () => openAdjustXpModal(targetUserId, safeName, xpVal);
      if (el.userModalBtnSetLevel) el.userModalBtnSetLevel.onclick = () => openSetLevelModal(targetUserId, safeName, levelVal);
      if (el.userModalBtnBanToggle) el.userModalBtnBanToggle.onclick = () => openBanModal(targetUserId, safeName, isBanned);
      if (el.userModalBtnResetStats) el.userModalBtnResetStats.onclick = () => confirmResetUserStats(targetUserId, safeName);
    } catch (err) {
      console.error("Error loading user profile:", err);
      alert("Foydalanuvchi ma'lumotlarini yuklashda xatolik yuz berdi");
      if (el.modalUserProfile) el.modalUserProfile.classList.add('hidden');
    }
  }

  if (el.btnCloseUserProfile) {
    el.btnCloseUserProfile.addEventListener('click', () => {
      if (el.modalUserProfile) el.modalUserProfile.classList.add('hidden');
      state.activeUserProfileId = null;
    });
  }

  // Modal 1: Adjust Points
  function openAdjustPointsModal(userId, name, currentPoints) {
    if (!el.modalAdjustPoints) return;
    if (el.modalAdjustPointsUserId) el.modalAdjustPointsUserId.value = userId;
    if (el.modalAdjustPointsSubtitle) el.modalAdjustPointsSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId}) | Hozirgi ball: ${currentPoints}`;
    if (el.inputNewPoints) el.inputNewPoints.value = currentPoints;
    el.modalAdjustPoints.classList.remove('hidden');
    if (el.inputNewPoints) el.inputNewPoints.focus();
  }

  if (el.btnCancelAdjustPoints) {
    el.btnCancelAdjustPoints.addEventListener('click', () => {
      if (el.modalAdjustPoints) el.modalAdjustPoints.classList.add('hidden');
    });
  }

  if (el.btnSaveAdjustPoints) {
    el.btnSaveAdjustPoints.addEventListener('click', async () => {
      const userId = el.modalAdjustPointsUserId ? el.modalAdjustPointsUserId.value : '';
      const newPoints = parseInt(el.inputNewPoints ? el.inputNewPoints.value : '', 10);
      if (isNaN(newPoints) || newPoints < 0) {
        alert("Yaroqli musbat ball kiriting.");
        return;
      }

      const res = await api('/api/admin/users/adjust-points', {
        method: 'POST',
        body: { user_id: parseInt(userId, 10), points: newPoints }
      });

      if (res.ok) {
        if (el.modalAdjustPoints) el.modalAdjustPoints.classList.add('hidden');
        loadUsers();
        loadRecentUsers();
        loadRecentUsersOverview();
        if (state.activeUserProfileId == userId) {
          openUserProfileModal(userId);
        }
      } else {
        alert(res.error || "Ballarni yangilashda xatolik");
      }
    });
  }

  // Modal 2: Adjust XP
  function openAdjustXpModal(userId, name, currentXp) {
    if (!el.modalAdjustXp) return;
    if (el.modalAdjustUserId) el.modalAdjustUserId.value = userId;
    if (el.modalAdjustXpSubtitle) el.modalAdjustXpSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId}) | Hozirgi XP: ${currentXp}`;
    if (el.inputNewXp) el.inputNewXp.value = currentXp;
    el.modalAdjustXp.classList.remove('hidden');
    if (el.inputNewXp) el.inputNewXp.focus();
  }

  if (el.btnCancelAdjustXp) {
    el.btnCancelAdjustXp.addEventListener('click', () => {
      if (el.modalAdjustXp) el.modalAdjustXp.classList.add('hidden');
    });
  }

  if (el.btnSaveAdjustXp) {
    el.btnSaveAdjustXp.addEventListener('click', async () => {
      const userId = el.modalAdjustUserId ? el.modalAdjustUserId.value : '';
      const newXp = parseInt(el.inputNewXp ? el.inputNewXp.value : '', 10);
      if (isNaN(newXp) || newXp < 0) {
        alert("Yaroqli musbat son kiriting.");
        return;
      }

      const res = await api('/api/admin/users/adjust-xp', {
        method: 'POST',
        body: { user_id: parseInt(userId, 10), xp: newXp }
      });

      if (res.ok) {
        if (el.modalAdjustXp) el.modalAdjustXp.classList.add('hidden');
        loadUsers();
        loadRecentUsers();
        loadRecentUsersOverview();
        if (state.activeUserProfileId == userId) {
          openUserProfileModal(userId);
        }
      } else {
        alert(res.error || "XP yangilashda xatolik");
      }
    });
  }

  // Modal 3: Set Level
  function openSetLevelModal(userId, name, currentLevel) {
    if (!el.modalSetLevel) return;
    if (el.modalSetLevelUserId) el.modalSetLevelUserId.value = userId;
    if (el.modalSetLevelSubtitle) el.modalSetLevelSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId}) | Hozirgi daraja: ${currentLevel}`;
    if (el.inputNewLevel) el.inputNewLevel.value = currentLevel;
    el.modalSetLevel.classList.remove('hidden');
    if (el.inputNewLevel) el.inputNewLevel.focus();
  }

  if (el.btnCancelSetLevel) {
    el.btnCancelSetLevel.addEventListener('click', () => {
      if (el.modalSetLevel) el.modalSetLevel.classList.add('hidden');
    });
  }

  if (el.btnSaveSetLevel) {
    el.btnSaveSetLevel.addEventListener('click', async () => {
      const userId = el.modalSetLevelUserId ? el.modalSetLevelUserId.value : '';
      const newLevel = parseInt(el.inputNewLevel ? el.inputNewLevel.value : '', 10);
      if (isNaN(newLevel) || newLevel < 1 || newLevel > 100) {
        alert("Daraja 1 dan 100 gacha bo'lishi kerak.");
        return;
      }

      const res = await api('/api/admin/users/set-level', {
        method: 'POST',
        body: { user_id: parseInt(userId, 10), level: newLevel }
      });

      if (res.ok) {
        if (el.modalSetLevel) el.modalSetLevel.classList.add('hidden');
        loadUsers();
        loadRecentUsers();
        loadRecentUsersOverview();
        if (state.activeUserProfileId == userId) {
          openUserProfileModal(userId);
        }
      } else {
        alert(res.error || "Darajani yangilashda xatolik");
      }
    });
  }

  // Modal 4: Ban / Unban
  function openBanModal(userId, name, isCurrentlyBanned) {
    if (!el.modalBanUser) return;
    if (el.modalBanUserId) el.modalBanUserId.value = userId;
    if (el.modalBanAction) el.modalBanAction.value = isCurrentlyBanned ? 'unban' : 'ban';
    if (el.modalBanSubtitle) el.modalBanSubtitle.textContent = `Foydalanuvchi: ${name} (ID: ${userId})`;

    if (isCurrentlyBanned) {
      if (el.modalBanTitle) el.modalBanTitle.innerHTML = `<i class="fa-solid fa-lock-open text-emerald-400"></i><span>Foydalanuvchini Blokdan Chiqarish</span>`;
      if (el.modalBanReasonContainer) el.modalBanReasonContainer.classList.add('hidden');
      if (el.btnConfirmBan) {
        el.btnConfirmBan.textContent = "Blokdan Ochish";
        el.btnConfirmBan.className = "w-1/2 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold transition";
      }
    } else {
      if (el.modalBanTitle) el.modalBanTitle.innerHTML = `<i class="fa-solid fa-ban text-rose-500"></i><span>Foydalanuvchini Bloklash</span>`;
      if (el.modalBanReasonContainer) el.modalBanReasonContainer.classList.remove('hidden');
      if (el.inputBanReason) el.inputBanReason.value = "";
      if (el.btnConfirmBan) {
        el.btnConfirmBan.textContent = "Bloklash";
        el.btnConfirmBan.className = "w-1/2 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-semibold transition";
      }
    }

    el.modalBanUser.classList.remove('hidden');
  }

  if (el.btnCancelBan) {
    el.btnCancelBan.addEventListener('click', () => {
      if (el.modalBanUser) el.modalBanUser.classList.add('hidden');
    });
  }

  if (el.btnConfirmBan) {
    el.btnConfirmBan.addEventListener('click', async () => {
      const userId = parseInt(el.modalBanUserId ? el.modalBanUserId.value : '', 10);
      const action = el.modalBanAction ? el.modalBanAction.value : 'ban';
      const isBan = action === 'ban';
      const reason = el.inputBanReason ? el.inputBanReason.value.trim() : '';

      const res = await api('/api/admin/users/ban', {
        method: 'POST',
        body: {
          user_id: userId,
          ban: isBan,
          reason: reason
        }
      });

      if (res.ok) {
        if (el.modalBanUser) el.modalBanUser.classList.add('hidden');
        loadUsers();
        loadRecentUsers();
        loadRecentUsersOverview();
        if (state.activeUserProfileId == userId) {
          openUserProfileModal(userId);
        }
      } else {
        alert(res.error || "Amalni bajarishda xatolik");
      }
    });
  }

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
      loadRecentUsersOverview();
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

  if (el.btnRefreshGroups) {
    el.btnRefreshGroups.addEventListener('click', () => loadGroups());
  }

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

    if (el.broadcastText) el.broadcastText.addEventListener('input', updatePreview);
    if (el.broadcastPhoto) el.broadcastPhoto.addEventListener('input', updatePreview);
    if (el.broadcastBtnText) el.broadcastBtnText.addEventListener('input', updatePreview);
    if (el.broadcastBtnUrl) el.broadcastBtnUrl.addEventListener('input', updatePreview);
  }

  function renderTelegramHtml(raw) {
    let clean = escapeHtml(raw);
    clean = clean.replace(/&lt;b&gt;(.*?)&lt;\/b&gt;/gi, '<b>$1</b>');
    clean = clean.replace(/&lt;i&gt;(.*?)&lt;\/i&gt;/gi, '<i>$1</i>');
    clean = clean.replace(/&lt;code&gt;(.*?)&lt;\/code&gt;/gi, '<code class="bg-black/30 px-1 rounded">$1</code>');
    clean = clean.replace(/\n/g, '<br>');
    return clean;
  }

  if (el.btnStartBroadcast) {
    el.btnStartBroadcast.addEventListener('click', async () => {
      const target = document.querySelector('input[name="broadcastTarget"]:checked')?.value || 'all';
      const text = el.broadcastText ? el.broadcastText.value.trim() : '';
      const photo = (el.broadcastPhoto && el.broadcastPhoto.value.trim()) || null;
      const btnText = (el.broadcastBtnText && el.broadcastBtnText.value.trim()) || null;
      const btnUrl = (el.broadcastBtnUrl && el.broadcastBtnUrl.value.trim()) || null;

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
          if (el.broadcastStatusTitle) el.broadcastStatusTitle.textContent = "Xabarnoma holati: Boshlandi...";
          if (el.broadcastSpinner) el.broadcastSpinner.classList.remove('hidden');
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
  }

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

  if (el.btnRefreshLogs) {
    el.btnRefreshLogs.addEventListener('click', () => loadLogs());
  }
  if (el.inputLogFilter) {
    el.inputLogFilter.addEventListener('input', () => loadLogs());
  }

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

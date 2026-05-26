/* AgentCounsel catalog — copy-to-clipboard for skill pages. */
(function () {
  'use strict';

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'absolute';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand('copy');
        resolve();
      } catch (e) {
        reject(e);
      } finally {
        document.body.removeChild(ta);
      }
    });
  }

  var filter = document.getElementById('skill-filter');
  if (filter) {
    var rows = document.querySelectorAll('[data-filter-row]');
    filter.addEventListener('input', function () {
      var q = filter.value.trim().toLowerCase();
      for (var k = 0; k < rows.length; k++) {
        var r = rows[k];
        var text = (r.getAttribute('data-filter-text') || r.textContent).toLowerCase();
        r.style.display = (!q || text.indexOf(q) !== -1) ? '' : 'none';
      }
    });
  }

  var buttons = document.querySelectorAll('[data-copy]');
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function () {
      var btn = this;
      var target = document.getElementById(btn.getAttribute('data-copy'));
      if (!target) return;
      var label = btn.textContent;
      copyText(target.textContent).then(function () {
        btn.textContent = 'Copied';
        btn.classList.add('copied');
      }, function () {
        btn.textContent = 'Copy failed';
      }).then(function () {
        setTimeout(function () {
          btn.textContent = label;
          btn.classList.remove('copied');
        }, 1600);
      });
    });
  }
})();

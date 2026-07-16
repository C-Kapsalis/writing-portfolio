// Open every external link in a new tab, safely.
// Internal navigation (same host, relative links) stays in the current tab.
document.addEventListener("DOMContentLoaded", function () {
  var anchors = document.querySelectorAll("a[href]");
  anchors.forEach(function (a) {
    // a.hostname is populated for absolute URLs; empty/relative -> internal.
    if (a.hostname && a.hostname !== window.location.hostname) {
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener noreferrer");
    }
  });
});

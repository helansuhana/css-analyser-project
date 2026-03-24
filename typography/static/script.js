function navigateTo(path) {
window.location.href = path;
}
function analyzeWebsite() {
  const url = document.getElementById("urlInput").value;

  if (!url) {
    alert("Please enter a website URL");
    return;
  }

  fetch("/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ website: url })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("layout").innerText = data.layout.join("\n");
      document.getElementById("typography").innerText = data.typography.join("\n");
      document.getElementById("color").innerText = data.color.join("\n");
      document.getElementById("box").innerText = data.box.join("\n");
      document.getElementById("flex").innerText = data.flex.join("\n");
      document.getElementById("animation").innerText = data.animation.join("\n");
    })
    .catch(err => console.error(err));
}


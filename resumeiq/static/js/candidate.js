function analyzeResume() {
  const resume = document.getElementById("resume").files[0];
  const targetRole = document.getElementById("targetRole").value;

  if (!resume) {
    alert("Please upload a resume");
    return;
  }

  const formData = new FormData();
  formData.append("resume", resume);
  formData.append("target_role", targetRole);

  fetch("/candidate/analyze", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {

      // ATS Circle Animation
      const circle = document.getElementById("atsCircle");
      const radius = 48;
      const circumference = 2 * Math.PI * radius;
      const offset = circumference - (data.ats_score / 100) * circumference;

      circle.style.strokeDasharray = circumference;
      circle.style.strokeDashoffset = offset;

      document.getElementById("atsText").textContent =
        `${data.ats_score}%`;

      // Best Role
      document.getElementById("bestRole").textContent =
        data.best_fit_role;

      // Role Fit Bar
      document.getElementById("roleFit").textContent =
        `${data.role_fit_percentage}%`;

      document.getElementById("roleBar").style.width =
        `${data.role_fit_percentage}%`;

      // Suggestions
      const list = document.getElementById("recommendations");
      list.innerHTML = "";

      data.recommendations.forEach(rec => {
        const li = document.createElement("li");
        li.textContent = rec;
        list.appendChild(li);
      });

      document.getElementById("resultCard").classList.remove("hidden");
    })
    .catch(() => {
      alert("Error analyzing resume");
    });
}
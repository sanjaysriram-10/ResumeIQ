function analyzeResume() {
  const file = document.getElementById("resume").files[0];
  const role = document.getElementById("targetRole").value;

  if (!file) {
    alert("Please upload a resume");
    return;
  }

  const formData = new FormData();
  formData.append("resume", file);
  formData.append("target_role", role);

  fetch("/candidate/analyze", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
        return;
      }

      document.getElementById("resultCard").classList.remove("hidden");

      document.getElementById("atsBar").style.width = data.ats_score + "%";
      document.getElementById("atsText").innerText = data.ats_score + "% ATS match";

      document.getElementById("bestRole").innerText = data.best_fit_role;
      document.getElementById("roleFit").innerText =
        data.role_fit_percentage + "% match";
      document.getElementById("roleFit").innerText =
        data.role_fit_percentage + "% role fit";

      document.getElementById("recommendations").innerHTML =
        data.recommendations.map(r => `<li>${r}</li>`).join("");
    });
}

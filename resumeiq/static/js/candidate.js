function analyzeResume() {
  const file = document.getElementById("resume").files[0];

  if (!file) {
    alert("Please upload a resume");
    return;
  }

  const formData = new FormData();
  formData.append("resume", file);

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
      document.getElementById("atsText").innerText =
        data.ats_score + "% ATS Match";

      const skillsList = document.getElementById("skills");
      skillsList.innerHTML = "";

      data.skills.forEach(skill => {
        const li = document.createElement("li");
        li.innerText = skill;
        skillsList.appendChild(li);
      });
    })
    .catch(() => {
      alert("Resume analysis failed");
    });
}
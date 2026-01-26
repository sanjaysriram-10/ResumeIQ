function analyzeCandidates() {
  const jd = document.getElementById("jd").value.trim();
  const resumes = document.getElementById("resumes").files;

  if (!jd || resumes.length === 0) {
    alert("Please provide Job Description and resumes");
    return;
  }

  const formData = new FormData();
  formData.append("job_description", jd);

  for (let i = 0; i < resumes.length; i++) {
    formData.append("resumes", resumes[i]);
  }

  fetch("/recruiter/analyze", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      const table = document.getElementById("resultTable");
      table.innerHTML = "";

      data.sort((a, b) => b.match_percentage - a.match_percentage);

      data.forEach(c => {
        let badge = "bg-red-500";
        if (c.match_percentage >= 70) badge = "bg-green-500";
        else if (c.match_percentage >= 40) badge = "bg-yellow-500";

        table.innerHTML += `
          <tr>
            <td class="p-3">${c.name}</td>
            <td class="p-3">
              <span class="text-white px-3 py-1 rounded ${badge}">
                ${c.match_percentage}%
              </span>
            </td>
            <td class="p-3">${c.best_role}</td>
            <td class="p-3">
              <a href="${c.resume_url}" target="_blank"
                 class="text-blue-600 hover:underline">
                 View
              </a>
            </td>
          </tr>
        `;
      });
    })
    .catch(() => alert("Error analyzing candidates"));
}
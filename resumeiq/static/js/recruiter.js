let latestResults = [];

function updateUploadCount() {
  const files = document.getElementById("resumes").files;
  const info = document.getElementById("uploadInfo");

  if (files.length > 0) {
    info.textContent = `${files.length} resumes selected`;
    info.classList.remove("hidden");
  } else {
    info.classList.add("hidden");
  }
}

function analyzeCandidates() {
  const jd = document.getElementById("jd").value.trim();
  const resumes = document.getElementById("resumes").files;
  const button = document.getElementById("matchBtn");
  const loading = document.getElementById("loading");
  const exportBtn = document.getElementById("exportBtn");

  if (!jd || resumes.length === 0) {
    alert("Please upload resumes and provide Job Description");
    return;
  }

  const formData = new FormData();
  formData.append("job_description", jd);

  for (let i = 0; i < resumes.length; i++) {
    formData.append("resumes", resumes[i]);
  }

  // UI state
  button.disabled = true;
  button.classList.add("opacity-50");

  fetch("/recruiter/analyze", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      latestResults = data;
      exportBtn.classList.remove("hidden");

      const table = document.getElementById("resultTable");
      table.innerHTML = "";

      data.sort((a, b) => b.match_percentage - a.match_percentage);

      data.forEach(c => {
        let badge = "bg-red-500";
        if (c.match_percentage >= 70) badge = "bg-green-500";
        else if (c.match_percentage >= 40) badge = "bg-yellow-500";

        table.innerHTML += `
  <tr class="hover:bg-gray-50 transition">
    <td class="p-3 text-gray-800 font-medium">
      ${c.name}
    </td>

    <td class="p-3">
      <span class="px-3 py-1 rounded-full text-white text-xs ${badge}">
        ${c.match_percentage}%
      </span>
    </td>

    <td class="p-3 text-gray-700">
      ${c.best_role}
    </td>

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
    .catch(() => alert("Error analyzing candidates"))
    .finally(() => {
      button.disabled = false;
      button.classList.remove("opacity-50");
      loading.classList.add("hidden");
    });
}

function exportCSV() {
  if (latestResults.length === 0) return;

  let csv = "Candidate,Match %,Best Role\n";
  latestResults.forEach(c => {
    csv += `${c.name},${c.match_percentage},${c.best_role}\n`;
  });

  const blob = new Blob([csv], { type: "text/csv" });
  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "matched_candidates.csv";
  a.click();

  window.URL.revokeObjectURL(url);
}
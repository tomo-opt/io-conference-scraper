async function loadData() {
  const [recordsResp, summaryResp] = await Promise.all([
    fetch('./data/latest_conferences.json'),
    fetch('./data/latest_run_summary.json')
  ]);
  const records = await recordsResp.json();
  const summary = await summaryResp.json();
  return { records, summary };
}

function render(records) {
  const tbody = document.querySelector('#results tbody');
  tbody.innerHTML = records.map(r => `
    <tr>
      <td>${r.conference_title || ''}</td>
      <td>${r.organization || ''}</td>
      <td>${r.start_date || r.event_date_text || ''}</td>
      <td><a href="${r.conference_url || r.source_page}" target="_blank" rel="noreferrer">source</a></td>
    </tr>
  `).join('');
  document.getElementById('count').textContent = `${records.length} records`;
}

function initFilters(allRecords) {
  const search = document.getElementById('search');
  const orgFilter = document.getElementById('orgFilter');
  const orgs = [...new Set(allRecords.map(r => r.organization).filter(Boolean))].sort();
  orgFilter.innerHTML += orgs.map(o => `<option value="${o}">${o}</option>`).join('');

  const apply = () => {
    const q = search.value.toLowerCase();
    const org = orgFilter.value;
    const filtered = allRecords.filter(r => {
      const hitQ = !q || `${r.conference_title} ${r.organization} ${r.summary}`.toLowerCase().includes(q);
      const hitO = !org || r.organization === org;
      return hitQ && hitO;
    });
    render(filtered);
  };
  search.addEventListener('input', apply);
  orgFilter.addEventListener('change', apply);
}

loadData().then(({ records, summary }) => {
  document.getElementById('runTime').textContent = `Latest run: ${summary.run_finished_at_utc || 'unknown'}`;
  render(records);
  initFilters(records);
}).catch((err) => {
  document.getElementById('runTime').textContent = `Failed to load data: ${err}`;
});

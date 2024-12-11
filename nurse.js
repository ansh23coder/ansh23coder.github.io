// Handle Form Submission
document.getElementById('patientForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form reload

    // Get Form Values
    const name = document.getElementById('patientName').value.trim();
    const bloodPressure = document.getElementById('bloodPressure').value.trim();
    const pulse = document.getElementById('pulse').value.trim();
    const spo2 = document.getElementById('spo2').value.trim();
    const temperature = document.getElementById('temperature').value.trim();

    // Validate Inputs
    if (!name || !bloodPressure || !pulse || !spo2 || !temperature) {
        alert('All fields are required!');
        return;
    }

    // Display Output
    const outputContent = `
        <strong>Patient Name:</strong> ${name}<br>
        <strong>Blood Pressure:</strong> ${bloodPressure}<br>
        <strong>Pulse:</strong> ${pulse} bpm<br>
        <strong>SpO2:</strong> ${spo2}%<br>
        <strong>Temperature:</strong> ${temperature}
    `;
    document.getElementById('outputContent').innerHTML = outputContent;

    // Clear Form
    document.getElementById('patientForm').reset();
});

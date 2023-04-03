const form = document.getElementById('form');
form.addEventListener('submit', getFormValue);

function getFormValue(event) {
    event.preventDefault();
    const number = form.querySelector('[name="number"]')
    const data = {
        number: number.value,
    }
    console.log(data);
    axios.post('/feedback/', data)
}
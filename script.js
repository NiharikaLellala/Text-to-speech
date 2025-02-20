document.getElementById('convertButton').addEventListener('click', () => {
    const text = document.getElementById('textInput').value;
    const language = document.getElementById('languageInput').value;
     fetch('/convert', {
    method: 'POST',
    headers: {
     'Content-Type': 'application/json'
     },
     body: JSON.stringify({ text, language })
    }) 
    then(response => response.json())
.then(data => {
alert(data.message);
 })
 .catch(error => {
console.error('Error:', error);
alert('Error generating speech.');
 });
});
document.getElementById('playButton').addEventListener('click', () => {
const audio = new Audio('/output.mp3');
audio.play(); 
}); 
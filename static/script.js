document.getElementById('send-btn').addEventListener('click', function() {
  sendMessage();
});

document.getElementById('user-input').addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    sendMessage();
  }
});

function scrollToBottom() {
  var chatBox = document.getElementById('chat-box');
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  var userInput = document.getElementById('user-input').value;
  fetch('/query-chembl', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: userInput }),
  })
  .then(response => response.json())
  .then(data => {
    displayMessage('user', userInput);
    displayMessage('bot', data.reply, true); // Assuming all bot messages are molecule info
    document.getElementById('user-input').value = '';
  })
  .catch((error) => {
    displayMessage('bot', 'Error: Could not reach the server.');
  });
}

function displayMessage(sender, message, isMoleculeInfo = false) {
  var messagesContainer = document.getElementById('messages');
  var messageElement = document.createElement('div');
  messageElement.className = `message-bubble ${sender}-message`;

  if (isMoleculeInfo) {
    // This is where the SMILES string is made clickable
    const smilesMatch = message.match(/SMILES: (\S+)/);
    if (smilesMatch) {
      const smiles = smilesMatch[1];
      message = message.replace(smilesMatch[0], `<span class="smiles-clickable" onclick="showSmilesImage('${smiles}')">${smilesMatch[0]}</span>`);
    }
    messageElement.innerHTML = message;
  } else {
    messageElement.textContent = message;
  }

  messagesContainer.appendChild(messageElement);
  scrollToBottom();
}

function showSmilesImage(smiles) {
  var imageUrl = `http://hulab.rxnfinder.org/smi2img/${encodeURIComponent(smiles)}?w=300&h=300`;
  var imagePopup = document.createElement('div');
  imagePopup.className = 'image-popup';
  imagePopup.innerHTML = `<img src="${imageUrl}" alt="Chemical Structure" /><div class="close-popup" onclick="closePopup(this)">×</div>`;
  document.body.appendChild(imagePopup);
}

function closePopup(element) {
  element.parentNode.remove();
}

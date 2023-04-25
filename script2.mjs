let value = 'sup';
export{value};

function refreshAccounts() {
  fetch('/accounts')
    .then(response => response.json())
    .then(accounts => {
      window.rgstrdAccLoad = accounts; // uploads the accounts in the client-side
      //console.log(window.rgstrdAccLoad);
    });
}

// call the function immediately and then repeat every second
refreshAccounts();
setInterval(refreshAccounts, 1000);
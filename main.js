fetch('/test')
         .then(function (response) {
             return response.json();
         }).then(function (text) {
             document.getElementById("bitCoinParagraph").innerHTML = "The price of Bitcoin is expected to be: " + text.btc_price
             document.getElementById("ethParagraph").innerHTML = "The price of Ethereum is expected to be: " + text.eth_price
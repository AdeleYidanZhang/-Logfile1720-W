console.log("Chrome extension gogo");




chrome.runtime.onMessage.addListener(gotMessage);

function gotMessage(msg, sender, sendResponse) {
    console.log(msg.txt);
    if (msg.txt==="hello"){
        let paragraphs = document.getElementsByTagName('p');

        for(elt of paragraphs){
        elt.style['background-color']='#FF00FF';
        }

    }
}
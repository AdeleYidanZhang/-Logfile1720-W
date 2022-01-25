console.log('Izumis gallery');

let filenames =[
    "Io&Callisto.jpg",
    "kitsune.jpg",
    "ginsuko.jpg",
    "2020.jpg"
];
let img = document.getElementsByTagName('img');
 
for (imgElt of img){
    let r= Math.floor(Math.random()*filenames.length);
    let file = 'artworks/'+filenames[r];
    let url=chrome.extension.getURL(file);
    imgElt.src =url;
    console.log(url);
}
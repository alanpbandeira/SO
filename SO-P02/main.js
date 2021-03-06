const {app, BrowserWindow} = require('electron');
const path = require('path');
const url = require('url');


let win;

function createWindow(){
  // Create Window
   win = new BrowserWindow({width:600, height:800, icon:__dirname+'/img/icon.png'});

   // Load Window
   win.loadURL(url.format({
     pathname: path.join(__dirname, 'index.html'),
     protocol: 'file:',
     slashes: true
   }));

   // win.webContents.openDevTools();

   win.on('close', () => {
     win = null;
   })

   // if (win.File && win.FileReader && win.FileList && win.Blob) {
   //     // Great success! All the File APIs are supported.
   // } else {
   //     app.alert('The File APIs are not fully supported in this browser.');
   // }

}

// Run create window
app.on('ready', createWindow);


// Quit when all windows are closed
app.on('window-all-closed', () => {
  if(process.platform !== 'darwin'){
    app.quit();
  }
});

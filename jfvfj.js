var fso = new ActiveXObject("Scripting.FileSystemObject");
// 2=overwrite, true=create if not exist, 0 = ASCII

varFileObject = fso.OpenTextFile("./Sachin.txt", 2, true,0);
var url = document.location.pathname;
varFileObject.write(url);
varFileObject.close();

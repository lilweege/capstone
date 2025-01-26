import AdmZip from 'adm-zip';

export const unzipFile = (zipPath, outputDir) => {
    const zip = new AdmZip(zipPath);
    zip.extractAllTo(outputDir);
};

export const zipFiles = (inputDir, outputPath) => {
    const zip = new AdmZip();
    zip.addLocalFolder(inputDir);
    zip.writeZip(outputPath);
};

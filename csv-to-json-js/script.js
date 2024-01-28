const fs = require('fs');
const csv = require('csv-parser');
const results = [];

const csvFilePath = '../fakedb.csv';
const jsonFilePath = './fakedb.json';

fs.createReadStream(csvFilePath)
  .pipe(csv({separator: ';'}))
  .on('data', (data) => results.push(data))
  .on('end', () => {
    // Writes parsed content from CSV to a JSON file
    fs.writeFileSync(jsonFilePath, JSON.stringify(results, null, 2));
    console.log(`Arquivo JSON gerado com sucesso em: ${jsonFilePath}`);
  });
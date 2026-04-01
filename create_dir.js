const fs = require('fs');
const path = require('path');

const dbDir = path.join('C:', 'Users', 'Arunkumar', 'Desktop', 'hc', 'database');
fs.mkdirSync(dbDir, { recursive: true });
console.log('Database directory created successfully');

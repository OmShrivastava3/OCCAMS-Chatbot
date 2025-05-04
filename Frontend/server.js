const express = require('express');
const app = express();
const port = 3001; // Different port than the Python backend

app.use(express.static('public'));

app.listen(port, () => {
    console.log(`Frontend server listening at http://localhost:${port}`);
});
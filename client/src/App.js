import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import UploadImage from "./pages/UploadImage";
import UploadData from "./pages/UploadData";
import DownloadData from "./pages/DownloadData";
import HomePage from "./pages/HomePage";
import "./styles.css";

function App() {
  return (
    <Router>
      <div className="container">
        <h1>AI Demo App</h1>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/upload-image">Upload Image</Link></li>
            <li><Link to="/upload-data">Analyze Text</Link></li>
            <li><Link to="/download-data">Download Data</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/upload-image" element={<UploadImage />} />
          <Route path="/upload-data" element={<UploadData />} />
          <Route path="/download-data" element={<DownloadData />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

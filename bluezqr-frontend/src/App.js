import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CandidateRegister from "../src/components/CandidateRegister";  // Adjust the path as needed
import StudentRegister from "../src/components/StudentRegister";      // 👈 New import
import Home from "../src/components/Home";                            // Optional home page

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} /> {/* Optional home page */}
        <Route path="/candidate-register" element={<CandidateRegister />} />
        <Route path="/student-register" element={<StudentRegister />} /> {/* 👈 New route */}
      </Routes>
    </Router>
  );
}

export default App;

import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img 
              src="/octofitapp-small.png" 
              alt="OctoFit Logo" 
              className="navbar-logo"
            />
            OctoFit Tracker
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/activities">
                  Activities
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">
                  Leaderboard
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">
                  Teams
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">
                  Users
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">
                  Workouts
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container-fluid">
        <Routes>
          <Route path="/" element={
            <div className="container mt-5 text-center">
              <h1 className="display-4 mb-4">Welcome to OctoFit Tracker</h1>
              <p className="lead mb-4">
                Track your fitness activities, compete with friends, and achieve your goals!
              </p>
              <div className="row mb-5">
                <div className="col-md-4 mb-3">
                  <div className="card">
                    <div className="card-body">
                      <h3 className="card-title">📊 Track Activities</h3>
                      <p className="card-text">Log your workouts and monitor your progress over time.</p>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-3">
                  <div className="card">
                    <div className="card-body">
                      <h3 className="card-title">🏆 Compete</h3>
                      <p className="card-text">Challenge your friends and climb the leaderboard.</p>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-3">
                  <div className="card">
                    <div className="card-body">
                      <h3 className="card-title">💪 Get Fit</h3>
                      <p className="card-text">Access personalized workout suggestions and achieve your fitness goals.</p>
                    </div>
                  </div>
                </div>
              </div>
              <div className="mt-4">
                <Link to="/activities" className="btn btn-primary btn-lg mx-2 mb-2">
                  📊 View Activities
                </Link>
                <Link to="/leaderboard" className="btn btn-success btn-lg mx-2 mb-2">
                  🏆 Leaderboard
                </Link>
                <Link to="/workouts" className="btn btn-info btn-lg mx-2 mb-2">
                  💪 Workouts
                </Link>
              </div>
            </div>
          } />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;

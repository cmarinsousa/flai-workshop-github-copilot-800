import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Leaderboard component mounted');
    console.log('Fetching from API endpoint:', API_URL);

    fetch(API_URL)
      .then(response => {
        console.log('Leaderboard API response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard raw data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard processed data:', leaderboardData);
        
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          Error loading leaderboard: {error}
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <span className="badge bg-success me-2">🏆</span>
        Leaderboard
      </h2>
      <div className="table-responsive">
        <table className="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">User</th>
              <th scope="col">Total Points</th>
              <th scope="col">Activities</th>
              <th scope="col">Total Distance (km)</th>
              <th scope="col">Total Calories</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => {
                let rankBadge = 'bg-primary';
                let rankEmoji = '';
                if (index === 0) {
                  rankBadge = 'bg-warning text-dark';
                  rankEmoji = '🥇';
                } else if (index === 1) {
                  rankBadge = 'bg-secondary';
                  rankEmoji = '🥈';
                } else if (index === 2) {
                  rankBadge = 'bg-danger';
                  rankEmoji = '🥉';
                }
                
                return (
                  <tr key={entry.id || index}>
                    <td>
                      <span className={`badge ${rankBadge}`}>
                        {rankEmoji} {index + 1}
                      </span>
                    </td>
                    <td><strong>{entry.username || 'N/A'}</strong></td>
                    <td>
                      <span className="badge bg-primary">{entry.points || 0}</span>
                    </td>
                    <td>{entry.total_activities || 0}</td>
                    <td>{entry.total_distance || 0}</td>
                    <td>
                      <span className="badge bg-success">{entry.total_calories || 0}</span>
                    </td>
                  </tr>
                );
              })
            ) : (
              <tr>
                <td colSpan="6" className="text-center text-muted">
                  <em>No leaderboard data available</em>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;

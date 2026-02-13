import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Teams component mounted');
    console.log('Fetching from API endpoint:', API_URL);

    fetch(API_URL)
      .then(response => {
        console.log('Teams API response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams raw data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams processed data:', teamsData);
        
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
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
          Error loading teams: {error}
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <span className="badge bg-info me-2">👥</span>
        Teams
      </h2>
      <div className="row">
        {teams.length > 0 ? (
          teams.map((team, index) => (
            <div key={team.id || index} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">
                    {team.name || 'Unnamed Team'}
                  </h5>
                  <p className="card-text">
                    {team.description || 'No description available'}
                  </p>
                  <ul className="list-unstyled">
                    <li>
                      <strong>Members:</strong> 
                      <span className="badge bg-primary ms-2">{team.member_count || 0}</span>
                    </li>
                    <li>
                      <strong>Created:</strong> {team.created_at ? new Date(team.created_at).toLocaleDateString() : 'N/A'}
                    </li>
                  </ul>
                  <div className="mt-3">
                    <button className="btn btn-sm btn-primary me-2">View Details</button>
                    <button className="btn btn-sm btn-success">Join Team</button>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info" role="alert">
              <strong>No teams found.</strong> Create a new team to get started!
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Teams;

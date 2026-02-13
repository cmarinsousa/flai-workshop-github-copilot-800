import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Users component mounted');
    console.log('Fetching from API endpoint:', API_URL);

    fetch(API_URL)
      .then(response => {
        console.log('Users API response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Users raw data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Users processed data:', usersData);
        
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
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
          Error loading users: {error}
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <span className="badge bg-primary me-2">👤</span>
        Users
      </h2>
      <div className="row">
        {users.length > 0 ? (
          users.map((user, index) => (
            <div key={user.id || index} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">
                    {user.username || 'Unknown User'}
                  </h5>
                  <p className="card-text">
                    <strong>Email:</strong> {user.email || 'N/A'}
                  </p>
                  <ul className="list-unstyled">
                    <li>
                      <strong>Team:</strong> 
                      <span className="badge bg-info ms-2">{user.team_name || user.team || 'No team'}</span>
                    </li>
                    <li>
                      <strong>Joined:</strong> {user.date_joined ? new Date(user.date_joined).toLocaleDateString() : 'N/A'}
                    </li>
                  </ul>
                  <div className="mt-3">
                    <button className="btn btn-sm btn-primary me-2">View Profile</button>
                    <button className="btn btn-sm btn-success">Message</button>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info" role="alert">
              <strong>No users found.</strong> Invite your friends to join!
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Users;

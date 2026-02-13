import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts component mounted');
    console.log('Fetching from API endpoint:', API_URL);

    fetch(API_URL)
      .then(response => {
        console.log('Workouts API response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts raw data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts processed data:', workoutsData);
        
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
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
          Error loading workouts: {error}
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <span className="badge bg-success me-2">💪</span>
        Workout Suggestions
      </h2>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout, index) => {
            let difficultyBadge = 'bg-secondary';
            if (workout.difficulty_level === 'Beginner') difficultyBadge = 'bg-success';
            else if (workout.difficulty_level === 'Intermediate') difficultyBadge = 'bg-warning text-dark';
            else if (workout.difficulty_level === 'Advanced') difficultyBadge = 'bg-danger';
            
            return (
              <div key={workout.id || index} className="col-md-6 col-lg-4 mb-4">
                <div className="card h-100">
                  <div className="card-body">
                    <h5 className="card-title">
                      {workout.name || 'Unnamed Workout'}
                    </h5>
                    <p className="card-text">
                      {workout.description || 'No description available'}
                    </p>
                    <ul className="list-unstyled">
                      <li>
                        <strong>Type:</strong> 
                        <span className="badge bg-info ms-2">{workout.activity_type || 'N/A'}</span>
                      </li>
                      <li>
                        <strong>Duration:</strong> {workout.duration || 0} min
                      </li>
                      <li>
                        <strong>Difficulty:</strong> 
                        <span className={`badge ${difficultyBadge} ms-2`}>{workout.difficulty_level || 'N/A'}</span>
                      </li>
                      <li>
                        <strong>Target Group:</strong> {workout.target_muscle_group || 'N/A'}
                      </li>
                    </ul>
                    <div className="mt-3">
                      <button className="btn btn-sm btn-primary me-2">View Details</button>
                      <button className="btn btn-sm btn-success">Start Workout</button>
                    </div>
                  </div>
                </div>
              </div>
            );
          })
        ) : (
          <div className="col-12">
            <div className="alert alert-info" role="alert">
              <strong>No workout suggestions found.</strong> Check back later for personalized recommendations!
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;

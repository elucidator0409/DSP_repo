import React from 'react'
import { Spinner } from 'react-bootstrap'

function loader() {
  return (
    <div className="text-center" style={{ margin: '2rem' }}>
      <Spinner animation="border"
              role="status"
              style={{ 
                  height:'100px',
                  width:'100px',
                  margin: 'auto',
                  display: 'block'
              }}
      >
          <span className="sr-only">Loading...</span>
      </Spinner>  

      <h1 className="display-5 mt-3">Loading</h1>
    </div>
  );
}

export default loader
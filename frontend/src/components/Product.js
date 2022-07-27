import React from 'react'
import { Card } from 'react-bootstrap'
import Rating from './Rating'
import { Link } from 'react-router-dom'
import defaultImage from '../constants/no-image.png'

const imageStyle = {
  width: "100%" 
}

function Product({ product }) {
  return (
    <Card className="my-3 p-3 rounded">
        <Link to={`/product/${product.id}`}>
            <img
            style={imageStyle}
            alt="The representation of an angle"
            onError={( { currentTarget } ) => {
              currentTarget.onerror = null; // prevents looping
              currentTarget.src="https://demofree.sirv.com/nope-not-here.jpg"
            }}
            src={'https://image.tmdb.org/t/p/original'+ product.poster_path} />
        </Link>

        <Card.Body>
            
            <Card.Title as="div">
                <Link  to={`/product/${product.id}`} >
                    <strong>{product.title}</strong>
                </Link>
            </Card.Title>

            

            <Card.Text as="div" >
                <div className="my-3">
                        <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'} />
                </div>
            </Card.Text>

            <Card.Text as="h3">
                ${product.price}
            </Card.Text>
        </Card.Body>
    </Card>
  )
}

export default Product
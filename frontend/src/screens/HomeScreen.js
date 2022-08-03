import React, { useEffect } from 'react'
import { Row, Col, Alert, Container } from 'react-bootstrap'

import { useDispatch, useSelector } from 'react-redux'
import Product from '../components/Product'
import Loader from '../components/Loader'
import Message from '../components/Message'
import Paginate from '../components/Paginate'
import { listProducts } from '../actions/productActions'


function HomeScreen({ history}) {
  const dispatch = useDispatch();
  const productList = useSelector(state => state.productList);
  const { error, loading, products, page, pages } = productList;
  
  let keyword = history.location.search;

  useEffect(() => {
    dispatch(listProducts(keyword))    
  },[dispatch, keyword])
  
  return (
    <div>
        <div className="card">
          <div className="card-body">
            <p className="card-text">This website provides the content-based filtering search functionalities, you can search for movies by plot!</p>
          </div>
        </div>
        <h1 className="display-6">Featured movies</h1>
        {
          loading ? <Loader />
          : error ? <Message>{error}</Message> 
          :
            <Container>
              <Row>
                  {products.map(product =>(
                      <Col key={product.id} sm={12} md={6} lg={4} xl={3}>
                          <Product product={product} />
                      </Col>
                  ))}
              </Row>
              <div style={{ display: 'flex',  justifyContent: 'center' }}>
                <Paginate page={page} pages={pages} keyword={keyword} />
              </div>
            </Container>
        }
    </div>
  );
}

export default HomeScreen


import React, {useState, useEffect } from 'react'
import { Row, Col } from 'react-bootstrap'

import { useDispatch, useSelector } from 'react-redux'
import Product from '../components/Product'
import Loader from '../components/Loader'
import Message from '../components/Message'
import Paginate from '../components/Paginate'
import ProductTop from '../components/ProductTop'
import { listProducts } from '../actions/productActions'
import axios from 'axios';


function HomeScreen({ history}) {
  const dispatch = useDispatch()
  const productList = useSelector(state => state.productList)
  const { error, loading, products, page, pages } = productList
  
  let keyword = history.location.search

  useEffect(() => {
    dispatch(listProducts(keyword))
    

    
  },[dispatch, keyword])
  

  return (
    <div>
        {/* {!keyword && <ProductTop />} */}
        <h1>Latest Products</h1>
        {loading ? <Loader />
                  : error ? <Message>{error}</Message> 
                    :
                    <div>
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
                    </div>
        }
        
    </div>
  )
}

export default HomeScreen


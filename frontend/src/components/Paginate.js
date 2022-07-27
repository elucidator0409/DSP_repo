import React from 'react'
import { Pagination } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

const calculateDisplay = ({ pages, page, keyword }) => {
     return (
      <>
      { 
        page > 1 
        ? <>
            <Pagination.Ellipsis />
            <LinkContainer 
              key={page-1}
              to={`/?keyword=${keyword}&page=${page-1}`}
              >
                <Pagination.Item active={false}>{page-1}</Pagination.Item>
            </LinkContainer>
          </>
        : ""
      }
        <LinkContainer 
          key={page}
          to={`/?keyword=${keyword}&page=${page}`}
          >
            <Pagination.Item active={true}>{page}</Pagination.Item>
        </LinkContainer>
        { 
        page < pages 
        ? <> 
            <LinkContainer 
              key={page+1}
              to={`/?keyword=${keyword}&page=${page+1}`}
              >
                <Pagination.Item active={false}>{page+1}</Pagination.Item>
            </LinkContainer>
            <Pagination.Ellipsis /> 
          </>
        : ""
      }
      </>
     )
}

function Paginate({pages, page ,keyword=''}) {
    if (keyword) {
        keyword = keyword.split('?keyword=')[1].split('&')[0]
    }


    if (pages > 1 && pages < 10) {
      return (
        <Pagination>
            {[...Array(pages).keys()].map((x) => (
              <LinkContainer 
              key={x + 1}
              to={`/?keyword=${keyword}&page=${x+1}`}
              >
                  <Pagination.Item active={x + 1 === page}>{x+1}</Pagination.Item>
              </LinkContainer>
            ))}

        </Pagination>
      );
    }

    if (pages > 10) {
      return (
        <Pagination>
            <LinkContainer 
              key={1}
              to={`/?keyword=${keyword}&page=${1}`}
              >
                <Pagination.First />
            </LinkContainer>
           { calculateDisplay({ page, pages, keyword }) }
            <LinkContainer 
              key={pages}
              to={`/?keyword=${keyword}&page=${pages}`}
              >
                <Pagination.Last />
            </LinkContainer>
        </Pagination>
      )
    }
}

export default Paginate
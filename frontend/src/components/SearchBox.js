import React, { useState } from 'react'
import { Button, Container, Form, FormGroup, Stack } from 'react-bootstrap'
import { useHistory } from 'react-router-dom'

function SearchBox() {
    const [keyword, setKeyword] = useState('')

    let history = useHistory()

    const submitHandler = (e) => {
        e.preventDefault()
        if (keyword) {
            history.push(`/search/?query=${keyword}`)
        } else {
            history.push(history.push(history.location.pathname))
        }
    }
    return (
        <Form onSubmit={submitHandler}>
          <Stack direction="horizontal" gap={3}>
          <FormGroup>
            <Form.Control
                type='text'
                name='q'
                onChange={(e) => setKeyword(e.target.value)}
                className='mr-sm-2 ml-sm-5'
            ></Form.Control>
          </FormGroup>
            
          <Button
              type='submit'
              variant='outline-success'
              className='p-2'
          >
              Submit
          </Button>
          </Stack>
        </Form>
    )
}

export default SearchBox
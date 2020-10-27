import './App.css';
import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      books: []
    };
    }
  componentDidMount(){
    this.getBooks();
  }

  getBooks(){
    axios
      .get('http://127.0.0.1:8000/api/v1/books')
      .then(res => {
        this.setState({ books: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }
  

  render() {
    return(
      <div>
        {this.state.books.map(
            book => (
              <div key={book.id}>
                <h3>{book.title}</h3>
                <h5>{book.category}</h5>
                <h5>{book.year}</h5>
                <h5>${book.price}</h5>
              </div>
            ))}
      </div>
    );
  }
}


export default App;

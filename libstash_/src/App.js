import './App.css';
import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      books: [],
      book_covers: []
    };
    }
  componentDidMount(){
    this.getBooks();
  }

  getBooks(){
    axios
      .get('http://127.0.0.1:8000/api/v1/books')
      .then(res => {
        this.setState({ books: res.data.results });
      })
      .catch(err => {
        console.log(err);
      });
  }
  
  getBookCover(x){
    var unique_id = x
    axios
      .get('http://127.0.0.1:8000/api/v1/book/' + { unique_id } + '/cover/')
      .then(res => {
        this.setState({ book_cover: res.data.results });

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
              <div key={book.unique_id}>
              {this.getBookCover(book.unique_id)}
                <h3>{book.title}</h3>
                <h3>{book.unique_id}</h3>
                {/* <img src={ this.state.book_cover }/> */}
                <h5>{book.category}</h5>
                <h5>{book.year}</h5>
                <h5>${book.price}</h5>
              </div>
            ))}
            <img src={this.state.book_covers}/>
      </div>
    );
  }
}

class 


export default App;

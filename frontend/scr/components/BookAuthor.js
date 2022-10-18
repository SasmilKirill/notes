import React from "react"
import {useParams} from "react-router-dom";

const BookItem = ({book}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors}
            </td>
        </tr>
    )
}


const BooksAuthors = ({books}) =>

   return (
       <table>
           <th>
               ID
           </th>
           <th>
               Name
           </th>
           <th>
               Authors
           </th>
           {books.map((book) => <BookItem book={book}/>)}
       </table>
   )
}


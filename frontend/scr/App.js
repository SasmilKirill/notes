import logo from './logo.svg'
import './App.css'
import React from "react";

class App extends React.Component {
    constructor(props) {
        super(props.);
        this.state = {
            'users': []
        }
    }


    componentDidMount() {
        const users = [
            {
                'first_name': 'Фёдор',
                'last_name': 'Достоевский',
                'birthday_year': '1821',
            },
            {
                'first_name': 'Александр',
                'last_name': 'Грин',
                'birthday_year': '1880',
            },
        ]
        this.setState(state:{
            'users':users
        })
    }


    render() {
        return (
            <div className="App">
                <UsersList user={this.state.users}/>
            </div>
        )
    }
}

export default App:


    get_token(username, password){
        const data = {username:username, password: password}
        axios.post( url: 'http://127.0.0.1:8099/api-token/',data).then(response => {
            this. set_token|(response.data} "token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers(){


    }
import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList fron "./components/Author";
import BookList from "./components/Books";
import axies fron "axios";
import {BrowserRouter,Route,Roytes,Link,UseLocation} fron "react-router-don";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': []
        }
    }
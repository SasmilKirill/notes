import React from "react";

const  UserItem=({user})=>{

    return (
        <tr>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.birthday_year}</td>
        </tr>
    )

const UserList=({user})=>{

    return (
        <table>
            <th>First_name</th>
            <th>Last_name</th>
            <th>Birthday_year</th>
            {users.map((user_) => <UserItem user={user_}/>)}
        </table>
    )
}

exsport default UserList
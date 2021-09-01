import { useState } from "react";
import { createUser } from "../../api/authentication/authAPI";
import { Redirect } from 'react-router'

const Signup = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    const [redirect, setRedirect] = useState(false)
    const [errorMessage, setErrorMessage] = useState([]) // handler for error message

    // Functions to reset the errorMessages back to none
    const clearState = () => {
        setErrorMessage([])
    }
    
    const handleChange = (e) => {
        if (e.target.name === 'username') {
            setUsername(e.target.value)
        } else if (e.target.name === 'password') {
            setPassword(e.target.value)
        } else if (e.target.name === 'email') {
            setEmail(e.target.value)
        }
    }

    const handleSubmit = (e) => {
        clearState(); // clears the current error messages if they exist
        e.preventDefault();
        const newUser = {
            username: username,
            password: password,
            email: email
        }
        createUser(newUser)
            .then( async (response) => { 
                if (response.status > 201) {
                    let error = await response.json()
                    if (error.username) {
                        //console.log("username: ",error.username[0])
                        setErrorMessage( arr => [...arr, "Username Error: " + error.username[0]])
                    }
                    if (error.email) {
                        //console.log("email: ", error.email[0])
                        setErrorMessage( arr => [...arr, "Email Error: " + error.email[0]])
                    }
                    if (error.password) {
                        //console.log("password: ", error.password[0])
                        setErrorMessage( arr => [...arr, "Password Error: " + error.password[0]])
                    }
                    // console.log("All Error: ", errorMessage)
                } else {
                    setRedirect(true)
                }})
    }
    
    if (redirect) {
        return <Redirect to = "/login"/>
    }

    return(
        <div>Signup
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input name="username" type="text" value={username} onChange={handleChange}/>
                </label>
                <label>
                    Password:
                    <input name="password" type="password" value={password} onChange={handleChange}/>
                </label>
                <label>
                    Email:
                    <input name="email" type="email" value={email} onChange={handleChange}/>
                </label>
                <input type="submit" value="Submit"/>
                { errorMessage && <ul className="error"> {errorMessage.map((item) => (<li>{item}</li>))} </ul>}
            </form>
        </div>
    )
}
export default Signup
import { useState, useEffect } from "react";
import { Redirect } from 'react-router';
import { register } from "../../api/scoring/scoringAPI";

const Register = () => {
    const [name, setName] = useState('')
    const [redirect, setRedirect] = useState(false)
    const [errorMessage, setErrorMessage] = useState([]) // handler for error message

    // Functions to reset the errorMessages back to none
    const clearState = () => {
        setErrorMessage([])
    }
    
    const handleChange = (e) => {
        if (e.target.name === 'name') {
            setName(e.target.value)
        }
    }

    const handleSubmit = (e) => {
        clearState(); // clears the current error messages if they exist
        e.preventDefault();
        const challenge = {
            points: 0,
            }
        register(challenge)
            .then( async (response) => { 
                if (response.status > 201) {
                    let error = await response.json()
                    if (error.flag) {
                        setErrorMessage( arr => [...arr, "Flag Error: " + error.flag[0]])
                    }
                    else { setRedirect(true) }
                }})
    }
    
    if (redirect) {
        return <Redirect to = "/login"/>
    }

    return(
        <div>Register for Challenges
            <form onSubmit={handleSubmit}>
                <label>
                    Current Challenges
                </label>
                <input type="submit" value="Submit"/>
                { errorMessage && <ul className="error"> {errorMessage.map((item) => (<li>{item}</li>))} </ul>}
            </form>
        </div>
    )
}

export default Register;
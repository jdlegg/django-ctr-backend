import { useState } from "react";
import { Redirect } from 'react-router'
import { scoreFlag } from "../../api/scoring/scoringAPI";

const Challenge1 = () => {

    const [flag, setFlag] = useState('')
    const [redirect, setRedirect] = useState(false)
    const [errorMessage, setErrorMessage] = useState([]) // handler for error message

    // Functions to reset the errorMessages back to none
    const clearState = () => {
        setErrorMessage([])
    }
    
    const handleChange = (e) => {
        if (e.target.name === 'flag') {
            setFlag(e.target.value)
        }
    }

    const handleSubmit = (e) => {
        clearState(); // clears the current error messages if they exist
        e.preventDefault();
        const newFlag = {
            name: "Web App 1",
            flag: flag,
        }
        scoreFlag(newFlag)
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
        <div>Challenge 1 Submission
            <p hidden>FLAG: test</p>
            <form onSubmit={handleSubmit}>
                <label>
                    Flag:
                    <input name="flag" type="text" value={flag} onChange={handleChange}/>
                </label>
                <input type="submit" value="Submit"/>
                { errorMessage && <ul className="error"> {errorMessage.map((item) => (<li>{item}</li>))} </ul>}
            </form>
        </div>
    )
}
export default Challenge1;
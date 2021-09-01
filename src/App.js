import { Route, Switch } from 'react-router-dom';
import Login from './components/authentication/login';
import Signup from './components/authentication/signup';
import Logout from './components/authentication/logout';
import Prote from './components/protected';
import Navbar from './components/Navbar';
import Score from './components/scoring/Score';
import Challenge1 from './components/challenges/challenge1';
import Register from './components/scoring/Register';
import { AppContext } from './context';
import { useEffect, useState } from 'react';

import './App.css';

function App() {

  const [ isAuth, setIsAuth ] = useState(false);

  useEffect(() => {
    if(localStorage.getItem('access_token')) {
      setIsAuth(true)
    }
  }, [])

  return (
    <AppContext.Provider value={{  }}>
      <div className="App">
        <Navbar isAuth={isAuth}/>
        <Switch>
          <Route exact path='/login' render={(props) => (<Login {...props} setIsAuth={setIsAuth} isAuth={isAuth} /> )} />
          <Route exact path={"/signup/"} component={Signup}/>
          <Route exact path='/logout' render={(props) => (<Logout {...props} setIsAuth={setIsAuth} isAuth={isAuth} /> )} />
          <Route exact path="/protected" render={(props) => (<Prote {...props} setIsAuth={setIsAuth} isAuth={isAuth} /> )} />
          <Route exact path="/challenge1" render={(props) => (<Challenge1 {...props} setIsAuth={setIsAuth} isAuth={isAuth} /> )} />
          <Route exact path="/register" render={(props) => (<Register {...props} setIsAuth={setIsAuth} isAuth={isAuth} /> )} />
          <Route exact path="/:name" render={(props) => (<Score {...props} setIsAuth={setIsAuth} isAuth={isAuth} /> )} />
        </Switch>
      </div>
    </AppContext.Provider>
  );
}

export default App;

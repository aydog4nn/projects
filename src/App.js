import Alert from "./components/Alert";
import Navbar from "./components/Navbar";
import Search from "./components/Search";
import UserList from "./components/UserList";

import React, { Component } from "react";

export class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: false,
      users: [],
      error: null,
    };
  }

  searchUsers = (keyword) => {
    this.setState({ loading: true });

    setTimeout(() => {
      fetch("https://api.github.com/search/users?q=" + keyword)
        .then((response) => response.json())
        .then((data) => this.setState({ users: data.items, loading: false }));
    }, 1000);
  };

  clearResults = () => {
    this.setState({ users: [] });
  };

  displayAlert = (msg, type) => {
    this.setState({ error: { msg: msg, type: type } });
 

    setTimeout(() => {
      this.setState({
        error:null
      })
    },3000)
  };
  render() {
    return (
      <div>
        <Navbar title="Github" />
        <Search
          searchUsers={this.searchUsers}
          clearResults={this.clearResults}
          displayAlert={this.displayAlert}
          showclearButton={this.state.users.length > 0 ? true : false}
        />
        <Alert error={this.state.error}/>
        <div className="container mt-3">
          <UserList users={this.state.users} loading={this.state.loading} />
        </div>
      </div>
    );
  }
}

export default App;

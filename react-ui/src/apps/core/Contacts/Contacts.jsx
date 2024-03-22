import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Contacts.styles';

class Contacts extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Contacts will mount');
  }

  componentDidMount = () => {
    console.log('Contacts mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Contacts will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Contacts will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Contacts did update');
  }

  componentWillUnmount = () => {
    console.log('Contacts will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="ContactsWrapper">
        Test content
      </div>
    );
  }
}

Contacts.propTypes = {
  // bla: PropTypes.string,
};

Contacts.defaultProps = {
  // bla: 'test',
};

const mapStateToProps = state => ({
  // blabla: state.blabla,
});

const mapDispatchToProps = dispatch => ({
  // fnBlaBla: () => dispatch(action.name()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Contacts);

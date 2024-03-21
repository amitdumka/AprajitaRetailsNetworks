import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './BankAccounts.styles';

class BankAccounts extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('BankAccounts will mount');
  }

  componentDidMount = () => {
    console.log('BankAccounts mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('BankAccounts will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('BankAccounts will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('BankAccounts did update');
  }

  componentWillUnmount = () => {
    console.log('BankAccounts will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="BankAccountsWrapper">
        Test content
      </div>
    );
  }
}

BankAccounts.propTypes = {
  // bla: PropTypes.string,
};

BankAccounts.defaultProps = {
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
)(BankAccounts);

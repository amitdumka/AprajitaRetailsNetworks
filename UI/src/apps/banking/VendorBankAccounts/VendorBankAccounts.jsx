import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './VendorBankAccounts.styles';

class VendorBankAccounts extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('VendorBankAccounts will mount');
  }

  componentDidMount = () => {
    console.log('VendorBankAccounts mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('VendorBankAccounts will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('VendorBankAccounts will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('VendorBankAccounts did update');
  }

  componentWillUnmount = () => {
    console.log('VendorBankAccounts will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="VendorBankAccountsWrapper">
        Test content
      </div>
    );
  }
}

VendorBankAccounts.propTypes = {
  // bla: PropTypes.string,
};

VendorBankAccounts.defaultProps = {
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
)(VendorBankAccounts);

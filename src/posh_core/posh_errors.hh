#ifndef __POSH_ERROR__
#define __POSH_ERROR__

#include <string>
#include <iostream>


class PoshException: public std::exception {
public:
	PoshException(std::string msg) :
		std::exception(),
		_msg(msg) {};

	virtual const char* what() const throw() {
		return _msg.c_str();
	}

protected:
	std::string _msg;
};

#endif 

// Copyright (c) 2003-2009, Jodd Team (jodd.org). All Rights Reserved.

package jodd.madvoc.component;

import jodd.petite.meta.PetiteInject;
import jodd.petite.meta.PetiteInitMethod;
import jodd.madvoc.ActionConfig;
import jodd.madvoc.MadvocUtil;
import jodd.util.StringPool;

/**
 * Maps action results to result path. Invoked just before the result itself.
 */
public class ResultMapper {

	@PetiteInject
	protected MadvocConfig madvocConfig;

	@PetiteInitMethod(order = 1)
	void resultMapperInit() {
		init();
	}

	/**
	 * Additional custom initialization, invoked after manager is ready.
	 */
	protected void init() {}


	/**
	 * Returns resolved alias result value or passed on, if alias doesn't exist.
	 */
	protected String resolveAlias(String resultValue) {
		StringBuilder result = new StringBuilder(resultValue.length());
		int i = 0;
		int len = resultValue.length();
		while (i < len) {
			int ndx = resultValue.indexOf('%', i);
			if (ndx == -1) {
				// alias markers not found
				resultValue = (i == 0 ? resultValue : resultValue.substring(i));
				String alias = madvocConfig.getResultAlias(resultValue);
				result.append(alias != null ? alias : resultValue);
				break;
			}
			result.append(resultValue.substring(i, ndx));
			ndx++;
			int ndx2 = resultValue.indexOf('%', ndx);
			String alias = (ndx2 == -1 ? resultValue.substring(ndx) : resultValue.substring(ndx, ndx2));

			// process alias
			alias = madvocConfig.getResultAlias(alias);
			if (alias != null) {
				result.append(alias);
			}
			i = ndx2 + 1;
		}

		// fix '//' as prefix - it may happens when aliases are used.
		i = 0; len = result.length();
		while (i < len) {
			if (result.charAt(i) != '/') {
				break;
			}
			i++;
		}
		if (i > 1) {
			return result.subSequence(i - 1, len).toString();
		}
		return result.toString();
	}

	/**
	 * Resolves result path from action configuration and result value.
	 * By default, the result value is appended to the class action path and method action path.
	 * If result value starts with path prefix, it represent complete path.
	 * Although result value may be null, result is never null.
	 */
	public String resolveResultPath(ActionConfig cfg, String resultValue) {

		// absolute paths
		if (resultValue != null) {
			if (resultValue.startsWith(StringPool.SLASH)) {
				return resolveAlias(resultValue);
			}
		}

		String resultPath = MadvocUtil.stripHttpMethodFromActionPath(cfg.actionPath);

		// strip extension part
		int dotNdx = MadvocUtil.lastIndexOfDotAfterSlash(resultPath);
		if (dotNdx != -1) {
			resultPath = resultPath.substring(0, dotNdx);
		}

		// method
		boolean addDot = true;
		if (resultValue != null) {
			int i = 0;
			while (i < resultValue.length()) {
				if (resultValue.charAt(i) != '#') {
					break;
				}
				dotNdx = MadvocUtil.lastIndexOfSlashDot(resultPath);
				if (dotNdx != -1) {
					resultPath = resultPath.substring(0, dotNdx);
					if (resultPath.charAt(dotNdx - 1) == '/') {
						addDot = false;
					}
				}
				i++;
			}
			if (i > 0) {
				resultValue = resultValue.substring(i);
			}
		}

		// finally
		if ((resultValue != null) && (resultValue.length() != 0)) {
			if (addDot) {
				resultPath += StringPool.DOT;	// result separator
			}
			resultPath += resultValue;
		}
		return resolveAlias(resultPath); 
	}


}
